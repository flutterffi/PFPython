"""Tests for the package-based backend structure in project 07."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = PROJECT_ROOT / "projects" / "07_backend_service_app"

if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from backend_app.api import build_preview, create_app
from backend_app.bootstrap import build_topic_service
from backend_app.settings import load_settings


def test_package_settings_have_expected_keys() -> None:
    settings = load_settings()
    assert "app_name" in settings
    assert "default_topic" in settings
    assert "max_results" in settings


def test_package_bootstrap_builds_service() -> None:
    service = build_topic_service()
    payload = service.build_topic_payload("FastAPI").to_dict()
    assert payload["topic"] == "fastapi"
    assert len(payload["lessons"]) >= 1


def test_package_api_preview_has_route() -> None:
    preview = build_preview()
    assert preview["sample_route"] == "GET /topics/{topic}"


def test_package_create_app_returns_preview_or_fastapi_app() -> None:
    app = create_app()
    if isinstance(app, dict):
        assert app["framework"] == "FastAPI not installed"
    else:
        route_paths = {getattr(route, "path", "") for route in app.routes}
        assert "/topics/{topic}" in route_paths
        assert "/health" in route_paths


def main() -> None:
    test_package_settings_have_expected_keys()
    test_package_bootstrap_builds_service()
    test_package_api_preview_has_route()
    test_package_create_app_returns_preview_or_fastapi_app()
    print("test_backend_app_package.py passed.")


if __name__ == "__main__":
    main()
