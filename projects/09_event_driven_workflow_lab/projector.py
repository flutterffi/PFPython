"""Projection builder for the event-driven workflow lab."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from models import DomainEvent


def build_projection(events: list[DomainEvent]) -> dict[str, object]:
    summary: dict[str, object] = {"topics": {}, "event_count": len(events)}
    for event in events:
        topic_bucket = summary["topics"].setdefault(event.topic, [])
        topic_bucket.append(event.event_type)
    return summary


def rebuild_projection(event_log: list[DomainEvent]) -> dict[str, object]:
    """Rebuild a read model from the full persisted event log."""

    projection = build_projection(event_log)
    projection["rebuilt"] = True
    projection["unique_topics"] = sorted(projection["topics"])
    return projection


def main() -> None:
    events = [
        DomainEvent("evt-1", "payment.requested", "payments", {"amount": 99}),
        DomainEvent("evt-2", "payment.authorized", "payments", {"status": "ok"}),
    ]
    print("Projector demo")
    print("=" * 14)
    print(build_projection(events))


if __name__ == "__main__":
    main()
