"""Practice common backend layers with a tiny runnable example."""

from dataclasses import dataclass


@dataclass
class LessonRecord:
    topic: str
    difficulty: str


class LessonRepository:
    """Data-access layer."""

    def __init__(self) -> None:
        self._records = [
            LessonRecord(topic="functions", difficulty="basic"),
            LessonRecord(topic="logging", difficulty="intermediate"),
            LessonRecord(topic="fastapi", difficulty="advanced"),
        ]

    def list_records(self) -> list[LessonRecord]:
        return list(self._records)


class LessonService:
    """Business-logic layer."""

    def __init__(self, repository: LessonRepository) -> None:
        self.repository = repository

    def recommended_topics(self, min_level: str) -> list[str]:
        order = {"basic": 1, "intermediate": 2, "advanced": 3}
        threshold = order[min_level]
        return [
            record.topic
            for record in self.repository.list_records()
            if order[record.difficulty] >= threshold
        ]


def api_handler(service: LessonService, min_level: str) -> dict[str, object]:
    """API boundary layer."""

    topics = service.recommended_topics(min_level=min_level)
    return {
        "min_level": min_level,
        "count": len(topics),
        "topics": topics,
    }


def main() -> None:
    repository = LessonRepository()
    service = LessonService(repository)
    response = api_handler(service=service, min_level="intermediate")

    print("Backend layers example")
    print("=" * 24)
    print(response)
    print("\nLayer summary:")
    print("- contract/output: response dictionary")
    print("- API boundary: api_handler")
    print("- service: LessonService")
    print("- repository: LessonRepository")


if __name__ == "__main__":
    main()
