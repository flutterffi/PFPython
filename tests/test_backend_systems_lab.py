"""Tests for the backend systems lab project."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = PROJECT_ROOT / "projects" / "08_backend_systems_lab"

if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from models import RequestContext
from service import SystemsLabService


def test_systems_lab_returns_success_for_authorized_request() -> None:
    service = SystemsLabService()
    context = RequestContext(
        request_id="req-test-1",
        subject="learner",
        topic="observability",
        scopes={"read:topics"},
        idempotency_key="idem-test-1",
    )

    result = service.handle_request(context)
    assert result["mode"] == "new"
    assert result["response"]["status"] == "ok"
    assert result["response"]["topic"]["topic"] == "observability"


def test_systems_lab_replays_same_idempotency_key() -> None:
    service = SystemsLabService()
    context = RequestContext(
        request_id="req-test-2",
        subject="learner",
        topic="cache",
        scopes={"read:topics"},
        idempotency_key="idem-test-2",
    )

    first = service.handle_request(context)
    second = service.handle_request(context)
    assert first["mode"] == "new"
    assert second["mode"] == "replay"


def test_systems_lab_forbidden_without_scope() -> None:
    service = SystemsLabService()
    context = RequestContext(
        request_id="req-test-3",
        subject="learner",
        topic="auth",
        scopes={"read:logs"},
        idempotency_key="idem-test-3",
    )

    result = service.handle_request(context)
    assert result["response"]["status"] == "forbidden"


def main() -> None:
    test_systems_lab_returns_success_for_authorized_request()
    test_systems_lab_replays_same_idempotency_key()
    test_systems_lab_forbidden_without_scope()
    print("test_backend_systems_lab.py passed.")


if __name__ == "__main__":
    main()
