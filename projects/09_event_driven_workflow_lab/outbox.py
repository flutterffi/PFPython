"""Outbox simulation for the event-driven workflow lab."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from models import DomainEvent


class OutboxStore:
    def __init__(self) -> None:
        self.pending: list[DomainEvent] = []

    def append(self, event: DomainEvent) -> None:
        self.pending.append(event)

    def flush(self) -> list[DomainEvent]:
        events = list(self.pending)
        self.pending.clear()
        return events


def main() -> None:
    store = OutboxStore()
    store.append(
        DomainEvent(
            event_id="evt-outbox",
            event_type="payment.requested",
            topic="payments",
            payload={"amount": 99},
        )
    )
    print("Outbox demo")
    print("=" * 11)
    print([event.to_dict() for event in store.flush()])


if __name__ == "__main__":
    main()
