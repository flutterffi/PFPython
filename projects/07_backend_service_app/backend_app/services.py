"""Package services for the backend practice app."""

try:
    from .models import TopicPayload
    from .repositories import LessonRepository
except ImportError:
    from models import TopicPayload
    from repositories import LessonRepository


class TopicService:
    def __init__(self, repository: LessonRepository, max_results: int) -> None:
        self.repository = repository
        self.max_results = max_results

    def build_topic_payload(self, topic: str) -> TopicPayload:
        normalized = topic.strip().lower()
        lessons = self.repository.list_by_topic(normalized)[: self.max_results]
        return TopicPayload(topic=normalized, lessons=lessons)


def main() -> None:
    service = TopicService(repository=LessonRepository(), max_results=2)
    print("Package services demo")
    print("=" * 20)
    print(service.build_topic_payload("FastAPI").to_dict())


if __name__ == "__main__":
    main()
