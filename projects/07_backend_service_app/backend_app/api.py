"""Package API layer for the backend practice app."""

try:
    from fastapi import FastAPI
except ImportError:  # pragma: no cover - optional dependency path
    FastAPI = None

try:
    from .bootstrap import build_topic_service
    from .settings import load_settings
except ImportError:
    from bootstrap import build_topic_service
    from settings import load_settings


def build_preview() -> dict[str, object]:
    settings = load_settings()
    service = build_topic_service()
    payload = service.build_topic_payload(str(settings["default_topic"]))
    return {
        "framework": "FastAPI not installed",
        "suggested_module": "app_main:app",
        "sample_route": "GET /topics/{topic}",
        "sample_payload": payload.to_dict(),
    }


def create_app() -> object:
    settings = load_settings()
    service = build_topic_service()

    if FastAPI is None:
        return build_preview()

    app = FastAPI(title=str(settings["app_name"]))

    @app.get("/topics/{topic}")
    def read_topic(topic: str) -> dict[str, object]:
        return service.build_topic_payload(topic).to_dict()

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "pfpython-backend-package"}

    return app


def main() -> None:
    print("Package API demo")
    print("=" * 16)
    print(create_app())


if __name__ == "__main__":
    main()
