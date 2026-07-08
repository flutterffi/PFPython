"""Package repositories for the backend practice app."""

try:
    from .models import LessonItem
except ImportError:
    from models import LessonItem


class LessonRepository:
    def __init__(self) -> None:
        self._catalog = {
            "python": [
                LessonItem(topic="functions", level="basic", minutes=20),
                LessonItem(topic="modules", level="intermediate", minutes=25),
                LessonItem(topic="testing", level="intermediate", minutes=30),
            ],
            "fastapi": [
                LessonItem(topic="routing", level="intermediate", minutes=25),
                LessonItem(topic="dependencies", level="advanced", minutes=30),
                LessonItem(topic="logging", level="advanced", minutes=20),
            ],
        }

    def list_by_topic(self, topic: str) -> list[LessonItem]:
        return list(self._catalog.get(topic, []))


def main() -> None:
    repository = LessonRepository()
    print("Package repositories demo")
    print("=" * 25)
    print(repository.list_by_topic("fastapi"))


if __name__ == "__main__":
    main()
