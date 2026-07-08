"""Project 07 models: simple backend data shapes."""

from dataclasses import asdict, dataclass


@dataclass
class LessonSummary:
    topic: str
    level: str
    minutes: int


@dataclass
class TopicResponse:
    topic: str
    lessons: list[LessonSummary]

    def to_dict(self) -> dict[str, object]:
        return {
            "topic": self.topic,
            "lessons": [asdict(lesson) for lesson in self.lessons],
        }


def main() -> None:
    response = TopicResponse(
        topic="fastapi",
        lessons=[LessonSummary(topic="fastapi", level="advanced", minutes=35)],
    )
    print("Models demo")
    print("=" * 11)
    print(response.to_dict())


if __name__ == "__main__":
    main()
