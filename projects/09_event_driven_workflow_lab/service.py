"""Service orchestration for the event-driven workflow lab."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from broker import EventBroker
from models import DomainEvent, WorkflowState
from outbox import OutboxStore
from projector import build_projection
from saga import advance_workflow, compensate_workflow


class WorkflowLabService:
    def __init__(self) -> None:
        self.outbox = OutboxStore()
        self.broker = EventBroker()

    def run_workflow(self, topic: str, fail_step: str | None = None) -> dict[str, object]:
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
        self.broker.publish(events)
        consumed = self.broker.consume()
        projection = build_projection(consumed)

        return {
            "state": state.to_dict(),
            "events": [event.to_dict() for event in consumed],
            "projection": projection,
        }


def main() -> None:
    service = WorkflowLabService()
    print("Workflow lab demo")
    print("=" * 17)
    print(service.run_workflow("payments"))


if __name__ == "__main__":
    main()
