"""Tests for projects/07_backend_service_app service and repository flow."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = PROJECT_ROOT / "projects" / "07_backend_service_app"

if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from config import load_settings
from repository import LessonRepository
from service import TopicService


def test_load_settings_has_expected_keys() -> None:
    settings = load_settings()
    assert "app_name" in settings
    assert "default_topic" in settings
    assert "max_results" in settings


def test_repository_returns_fastapi_lessons() -> None:
    repository = LessonRepository()
    lessons = repository.fetch_by_topic("fastapi")
    assert len(lessons) >= 2
    assert lessons[0].topic == "routing"


def test_service_normalizes_topic_and_limits_results() -> None:
    service = TopicService(repository=LessonRepository(), max_results=2)
    response = service.get_topic_response("FastAPI")
    payload = response.to_dict()

    assert payload["topic"] == "fastapi"
    assert len(payload["lessons"]) == 2


def main() -> None:
    test_load_settings_has_expected_keys()
    test_repository_returns_fastapi_lessons()
    test_service_normalizes_topic_and_limits_results()
    print("test_backend_service_app.py passed.")


if __name__ == "__main__":
    main()
