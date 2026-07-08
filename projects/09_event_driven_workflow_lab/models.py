"""Shared models for the event-driven workflow lab."""

from dataclasses import asdict, dataclass


@dataclass
class DomainEvent:
    event_id: str
    event_type: str
    topic: str
    payload: dict[str, object]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass
class WorkflowState:
    workflow_id: str
    topic: str
    status: str
    steps: list[str]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def main() -> None:
    event = DomainEvent(
        event_id="evt-1",
        event_type="payment.requested",
        topic="payments",
        payload={"amount": 99},
    )
    print("Workflow models demo")
    print("=" * 20)
    print(event.to_dict())


if __name__ == "__main__":
    main()
