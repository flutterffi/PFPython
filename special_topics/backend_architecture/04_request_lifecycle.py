"""Practice tracing a backend request through validation, service, and response."""

from dataclasses import dataclass


@dataclass
class LessonQuery:
    topic: str


def validate_query(raw_topic: str) -> LessonQuery:
    topic = raw_topic.strip().lower()
    if not topic:
        raise ValueError("topic must not be empty")
    return LessonQuery(topic=topic)


class SearchService:
    def search(self, query: LessonQuery) -> list[str]:
        catalog = {
            "logging": ["logging basics", "json logging", "request tracing"],
            "fastapi": ["routing", "dependencies", "bigger applications"],
            "testing": ["unit tests", "mocking", "api test clients"],
        }
        return catalog.get(query.topic, ["no matching lessons yet"])


def build_response(topic: str, lessons: list[str]) -> dict[str, object]:
    return {
        "topic": topic,
        "count": len(lessons),
        "lessons": lessons,
    }


def main() -> None:
    raw_topic = "FastAPI"
    query = validate_query(raw_topic)
    service = SearchService()
    lessons = service.search(query)
    response = build_response(query.topic, lessons)

    print("Request lifecycle example")
    print("=" * 25)
    print(f"input -> {raw_topic!r}")
    print(f"validated -> {query}")
    print(f"service result -> {lessons}")
    print(f"response -> {response}")


if __name__ == "__main__":
    main()
