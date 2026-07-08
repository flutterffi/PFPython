"""Cache-aside simulation for the backend systems lab."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from models import TopicSummary


class TopicCache:
    def __init__(self) -> None:
        self._entries: dict[str, TopicSummary] = {}

    def get(self, topic: str) -> TopicSummary | None:
        return self._entries.get(topic)

    def set(self, summary: TopicSummary) -> None:
        self._entries[summary.topic] = summary


def main() -> None:
    cache = TopicCache()
    cache.set(TopicSummary(topic="observability", source="repository", message="warm"))
    print("Cache lab demo")
    print("=" * 14)
    print(cache.get("observability"))


if __name__ == "__main__":
    main()
