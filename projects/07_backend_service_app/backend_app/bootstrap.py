"""Package bootstrap for the backend practice app."""

try:
    from .repositories import LessonRepository
    from .services import TopicService
    from .settings import load_settings
except ImportError:
    from repositories import LessonRepository
    from services import TopicService
    from settings import load_settings


def build_topic_service() -> TopicService:
    settings = load_settings()
    return TopicService(
        repository=LessonRepository(),
        max_results=int(settings["max_results"]),
    )


def main() -> None:
    service = build_topic_service()
    print("Package bootstrap demo")
    print("=" * 21)
    print(service.build_topic_payload("python").to_dict())


if __name__ == "__main__":
    main()
