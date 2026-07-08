"""Package models for the backend practice app."""

from dataclasses import asdict, dataclass


@dataclass
class LessonItem:
    topic: str
    level: str
    minutes: int


@dataclass
class TopicPayload:
    topic: str
    lessons: list[LessonItem]

    def to_dict(self) -> dict[str, object]:
        return {
            "topic": self.topic,
            "lessons": [asdict(lesson) for lesson in self.lessons],
        }


def main() -> None:
    payload = TopicPayload(
        topic="fastapi",
        lessons=[LessonItem(topic="routing", level="intermediate", minutes=25)],
    )
    print("Package models demo")
    print("=" * 19)
    print(payload.to_dict())


if __name__ == "__main__":
    main()
