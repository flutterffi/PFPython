"""Show good and bad dependency flow in a small Python app."""


class LessonRepository:
    def load_topics(self) -> list[str]:
        return ["variables", "functions", "packages", "testing"]


class LessonService:
    def __init__(self, repository: LessonRepository) -> None:
        self.repository = repository

    def recommended_topics(self) -> list[str]:
        topics = self.repository.load_topics()
        return [topic for topic in topics if len(topic) >= 8]


class ConsoleView:
    def show_topics(self, topics: list[str]) -> None:
        print("Recommended longer topics:")
        for topic in topics:
            print(f"- {topic}")


def explain_rules() -> None:
    print("\nDependency direction rules")
    print("=" * 28)
    print("Good: interface -> service -> repository")
    print("Good: service knows repository contracts")
    print("Avoid: repository printing UI messages")
    print("Avoid: domain objects importing CLI code")
    print("Avoid: circular imports between layers")


def main() -> None:
    repository = LessonRepository()
    service = LessonService(repository)
    view = ConsoleView()

    topics = service.recommended_topics()
    view.show_topics(topics)
    explain_rules()


if __name__ == "__main__":
    main()
