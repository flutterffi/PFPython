"""Project 07 repository: in-memory backend data access."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from models import LessonSummary


class LessonRepository:
    def __init__(self) -> None:
        self._catalog = {
            "python": [
                LessonSummary(topic="functions", level="basic", minutes=20),
                LessonSummary(topic="modules", level="intermediate", minutes=25),
                LessonSummary(topic="testing", level="intermediate", minutes=30),
            ],
            "fastapi": [
                LessonSummary(topic="routing", level="intermediate", minutes=25),
                LessonSummary(topic="dependencies", level="advanced", minutes=30),
                LessonSummary(topic="logging", level="advanced", minutes=20),
            ],
        }

    def fetch_by_topic(self, topic: str) -> list[LessonSummary]:
        return list(self._catalog.get(topic, []))


def main() -> None:
    repository = LessonRepository()
    print("Repository demo")
    print("=" * 15)
    print(repository.fetch_by_topic("fastapi"))


if __name__ == "__main__":
    main()
