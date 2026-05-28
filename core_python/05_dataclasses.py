"""Core lesson 05: dataclasses for lightweight models."""

from dataclasses import dataclass, field


@dataclass
class LessonRecord:
    title: str
    minutes: int
    tags: list[str] = field(default_factory=list)

    def summary(self) -> str:
        tag_text = ", ".join(self.tags) if self.tags else "no tags"
        return f"{self.title}: {self.minutes} minutes ({tag_text})"


def main() -> None:
    record = LessonRecord("Decorators", 30, ["core", "functions"])
    print(record)
    print(record.summary())


if __name__ == "__main__":
    main()
