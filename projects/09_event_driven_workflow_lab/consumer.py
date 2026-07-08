"""Consumer-side deduplication for the event-driven workflow lab."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from models import DomainEvent


class DeduplicatingConsumer:
    def __init__(self) -> None:
        self.seen_event_ids: set[str] = set()
        self.processed: list[DomainEvent] = []
        self.duplicates: list[DomainEvent] = []

    def consume(self, events: list[DomainEvent]) -> dict[str, object]:
        for event in events:
            if event.event_id in self.seen_event_ids:
                self.duplicates.append(event)
                continue

            self.seen_event_ids.add(event.event_id)
            self.processed.append(event)

        return {
            "processed_count": len(self.processed),
            "duplicate_count": len(self.duplicates),
        }


def main() -> None:
    consumer = DeduplicatingConsumer()
    event = DomainEvent(
        event_id="evt-dup-1",
        event_type="payments.published",
        topic="payments",
        payload={"workflow_id": "wf-payments"},
    )
    report = consumer.consume([event, event])
    print("Consumer demo")
    print("=" * 13)
    print(report)


if __name__ == "__main__":
    main()
