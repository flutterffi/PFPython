"""Project 07 routes: optional FastAPI-style route wiring."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from config import load_settings
from repository import LessonRepository
from service import TopicService

try:
    from fastapi import FastAPI
except ImportError:  # pragma: no cover - optional dependency path
    FastAPI = None


def build_route_preview() -> dict[str, object]:
    settings = load_settings()
    service = TopicService(
        repository=LessonRepository(),
        max_results=int(settings["max_results"]),
    )
    sample = service.get_topic_response(str(settings["default_topic"]))
    return {
        "framework": "FastAPI not installed",
        "sample_route": "GET /topics/{topic}",
        "sample_response": sample.to_dict(),
    }


def create_app() -> object:
    settings = load_settings()
    service = TopicService(
        repository=LessonRepository(),
        max_results=int(settings["max_results"]),
    )

    if FastAPI is None:
        return build_route_preview()

    app = FastAPI(title=str(settings["app_name"]))

    @app.get("/topics/{topic}")
    def read_topic(topic: str) -> dict[str, object]:
        return service.get_topic_response(topic).to_dict()

    return app


def main() -> None:
    app = create_app()
    print("Routes demo")
    print("=" * 11)
    print(app)
    if FastAPI is None:
        print("\nNext step:")
        print("pip install fastapi uvicorn")
        print("Then move this example into a regular module name such as app_main.py")


if __name__ == "__main__":
    main()
