"""Lesson 09: classes, instance attributes, and methods."""


class StudySession:
    def __init__(self, topic: str, minutes: int) -> None:
        self.topic = topic
        self.minutes = minutes

    def describe(self) -> str:
        return f"StudySession(topic={self.topic}, minutes={self.minutes})"

    def is_long(self) -> bool:
        return self.minutes >= 45


def main() -> None:
    session = StudySession(topic="modules", minutes=50)
    print(session.describe())
    print(f"Long session? {session.is_long()}")


if __name__ == "__main__":
    main()
