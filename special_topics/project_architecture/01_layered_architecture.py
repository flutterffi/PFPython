"""Practice layered architecture with a small runnable example."""

from dataclasses import dataclass


@dataclass
class StudyTask:
    topic: str
    minutes: int
    done: bool = False


class TaskRepository:
    """Persistence-oriented layer."""

    def __init__(self) -> None:
        self._tasks = [
            StudyTask(topic="functions", minutes=25),
            StudyTask(topic="modules", minutes=30),
            StudyTask(topic="testing", minutes=35),
        ]

    def list_tasks(self) -> list[StudyTask]:
        return list(self._tasks)


class StudyPlannerService:
    """Application logic layer."""

    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def build_plan(self) -> list[str]:
        tasks = self.repository.list_tasks()
        return [
            f"Study {task.topic} for {task.minutes} minutes"
            for task in tasks
            if not task.done
        ]


def render_console(plan_lines: list[str]) -> None:
    """Interface layer."""

    print("Layered architecture example")
    print("=" * 32)
    for index, line in enumerate(plan_lines, start=1):
        print(f"{index}. {line}")


def main() -> None:
    repository = TaskRepository()
    service = StudyPlannerService(repository)
    plan_lines = service.build_plan()
    render_console(plan_lines)

    print("\nLayer responsibilities:")
    print("- domain: StudyTask")
    print("- repository: TaskRepository")
    print("- service: StudyPlannerService")
    print("- interface: render_console")


if __name__ == "__main__":
    main()
