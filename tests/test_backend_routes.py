"""Tests for projects/07_backend_service_app route preview behavior."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = PROJECT_ROOT / "projects" / "07_backend_service_app"

if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from routes import build_route_preview, create_app


def test_build_route_preview_has_sample_route() -> None:
    preview = build_route_preview()
    assert preview["sample_route"] == "GET /topics/{topic}"
    assert "sample_response" in preview


def test_create_app_returns_preview_or_fastapi_app() -> None:
    app = create_app()
    if isinstance(app, dict):
        assert app["framework"] == "FastAPI not installed"
    else:
        route_paths = {getattr(route, "path", "") for route in app.routes}
        assert "/topics/{topic}" in route_paths


def main() -> None:
    test_build_route_preview_has_sample_route()
    test_create_app_returns_preview_or_fastapi_app()
    print("test_backend_routes.py passed.")


if __name__ == "__main__":
    main()
