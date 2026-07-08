"""Practice app bootstrap and entrypoint wiring."""

from dataclasses import dataclass


@dataclass
class AppConfig:
    learner_name: str
    max_items: int


class MemoryNoteRepository:
    def __init__(self) -> None:
        self._notes = [
            "Review list comprehensions",
            "Refactor sqlite project layers",
            "Add tests for study assistant",
            "Extract config loader",
        ]

    def load_notes(self, limit: int) -> list[str]:
        return self._notes[:limit]


class StudyDashboardService:
    def __init__(self, repository: MemoryNoteRepository, config: AppConfig) -> None:
        self.repository = repository
        self.config = config

    def summary_lines(self) -> list[str]:
        notes = self.repository.load_notes(self.config.max_items)
        return [f"{self.config.learner_name}: {note}" for note in notes]


def build_app() -> StudyDashboardService:
    """Bootstrap is where objects are wired together."""

    config = AppConfig(learner_name="Learner", max_items=3)
    repository = MemoryNoteRepository()
    return StudyDashboardService(repository=repository, config=config)


def main() -> None:
    app = build_app()

    print("Bootstrap and entrypoint example")
    print("=" * 32)
    for line in app.summary_lines():
        print(line)

    print("\nWhy bootstrap matters:")
    print("- setup lives in one place")
    print("- dependencies are easy to swap")
    print("- tests can construct smaller pieces directly")
    print("- entrypoints stay short and readable")


if __name__ == "__main__":
    main()
