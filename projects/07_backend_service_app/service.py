"""Project 07 service: backend business logic."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from models import TopicResponse
from repository import LessonRepository


class TopicService:
    def __init__(self, repository: LessonRepository, max_results: int = 3) -> None:
        self.repository = repository
        self.max_results = max_results

    def get_topic_response(self, topic: str) -> TopicResponse:
        normalized = topic.strip().lower()
        lessons = self.repository.fetch_by_topic(normalized)[: self.max_results]
        return TopicResponse(topic=normalized, lessons=lessons)


def main() -> None:
    service = TopicService(repository=LessonRepository(), max_results=2)
    response = service.get_topic_response("FastAPI")
    print("Service demo")
    print("=" * 12)
    print(response.to_dict())


if __name__ == "__main__":
    main()
