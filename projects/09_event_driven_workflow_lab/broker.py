"""Broker simulation for the event-driven workflow lab."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from models import DomainEvent


class EventBroker:
    def __init__(self) -> None:
        self.published: list[DomainEvent] = []

    def publish(self, events: list[DomainEvent]) -> None:
        self.published.extend(events)

    def consume(self) -> list[DomainEvent]:
        return list(self.published)


def main() -> None:
    broker = EventBroker()
    event = DomainEvent(
        event_id="evt-broker",
        event_type="payment.authorized",
        topic="payments",
        payload={"status": "ok"},
    )
    broker.publish([event])
    print("Broker demo")
    print("=" * 11)
    print([item.to_dict() for item in broker.consume()])


if __name__ == "__main__":
    main()
