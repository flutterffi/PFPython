"""Core lesson 08: protocols for duck-typed interfaces."""

from typing import Protocol


class HasSummary(Protocol):
    def summary(self) -> str:
        ...


class Lesson:
    def __init__(self, title: str) -> None:
        self.title = title

    def summary(self) -> str:
        return f"Lesson summary: {self.title}"


class Project:
    def __init__(self, name: str) -> None:
        self.name = name

    def summary(self) -> str:
        return f"Project summary: {self.name}"


def print_summary(item: HasSummary) -> None:
    print(item.summary())


def main() -> None:
    print_summary(Lesson("Protocols"))
    print_summary(Project("Study Tracker"))


if __name__ == "__main__":
    main()
