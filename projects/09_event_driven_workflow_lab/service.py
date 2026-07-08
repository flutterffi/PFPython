"""Service orchestration for the event-driven workflow lab."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from broker import EventBroker
from consumer import DeduplicatingConsumer
from models import DomainEvent, WorkflowState
from outbox import OutboxStore
from projector import build_projection, rebuild_projection
from resilience import CircuitBreaker, RetryPolicy, execute_with_retry
from saga import advance_workflow, compensate_workflow


class WorkflowLabService:
    def __init__(self) -> None:
        self.outbox = OutboxStore()
        self.broker = EventBroker()
        self.consumer = DeduplicatingConsumer()
        self.retry_policy = RetryPolicy(max_attempts=3)
        self.circuit_breaker = CircuitBreaker(failure_threshold=2)

    def run_workflow(
        self,
        topic: str,
        fail_step: str | None = None,
        duplicate_publish: bool = False,
        publish_fail_times: int = 0,
    ) -> dict[str, object]:
        state = WorkflowState(workflow_id=f"wf-{topic}", topic=topic, status="started", steps=["requested"])
        self.outbox.append(
            DomainEvent(
                event_id=f"evt-{topic}-requested",
                event_type=f"{topic}.requested",
                topic=topic,
                payload={"workflow_id": state.workflow_id},
            )
        )

        state = advance_workflow(state, "validated")
        self.outbox.append(
            DomainEvent(
                event_id=f"evt-{topic}-validated",
                event_type=f"{topic}.validated",
                topic=topic,
                payload={"workflow_id": state.workflow_id},
            )
        )

        if fail_step == "publish":
            state = compensate_workflow(state, "publish")
            self.outbox.append(
                DomainEvent(
                    event_id=f"evt-{topic}-compensated",
                    event_type=f"{topic}.compensated",
                    topic=topic,
                    payload={"workflow_id": state.workflow_id},
                )
            )
        else:
            state = advance_workflow(state, "published")
            self.outbox.append(
                DomainEvent(
                    event_id=f"evt-{topic}-published",
                    event_type=f"{topic}.published",
                    topic=topic,
                    payload={"workflow_id": state.workflow_id},
                )
            )

        events = self.outbox.flush()
        publish_result = execute_with_retry(
            action_name="publish-events",
            fail_times=publish_fail_times,
            retry_policy=self.retry_policy,
            circuit_breaker=self.circuit_breaker,
        )
        if publish_result["status"] == "succeeded":
            self.broker.publish(events)
            if duplicate_publish:
                self.broker.publish(events)
        elif publish_result["status"] == "blocked":
            state = compensate_workflow(state, "circuit-open")
        else:
            state = compensate_workflow(state, "publish-retries-exhausted")

        consumed = self.broker.consume()
        consumer_report = self.consumer.consume(consumed)
        projection = build_projection(self.consumer.processed)
        rebuilt_projection = rebuild_projection(self.broker.replay())

        return {
            "state": state.to_dict(),
            "publish_result": publish_result,
            "events": [event.to_dict() for event in consumed],
            "consumer_report": consumer_report,
            "projection": projection,
            "rebuilt_projection": rebuilt_projection,
        }


def main() -> None:
    service = WorkflowLabService()
    print("Workflow lab demo")
    print("=" * 17)
    print(service.run_workflow("payments"))


if __name__ == "__main__":
    main()
