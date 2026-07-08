"""Tests for high-level backend scale pattern exercises."""

from pathlib import Path
import importlib.util


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TOPIC_DIR = PROJECT_ROOT / "special_topics" / "backend_scale_patterns"


def load_module(filename: str, module_name: str):
    module_path = TOPIC_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_idempotency_replays_same_response() -> None:
    module = load_module("03_idempotency_and_retry_control.py", "idempotency_module")
    processor = module.PaymentProcessor()
    request = module.ChargeRequest(
        idempotency_key="same-key",
        user_id="user-1",
        amount=50,
    )

    first = processor.charge(request)
    second = processor.charge(request)

    assert first["mode"] == "new"
    assert second["mode"] == "replay"
    assert first["response"] == second["response"]


def test_sli_report_uses_latency_and_status() -> None:
    module = load_module("05_observability_and_sli.py", "sli_module")
    samples = [
        module.RequestSample(latency_ms=80, status_code=200),
        module.RequestSample(latency_ms=170, status_code=200),
        module.RequestSample(latency_ms=300, status_code=503),
    ]

    report = module.calculate_sli(samples, latency_budget_ms=150)
    assert report["total_requests"] == 3
    assert report["availability_sli"] == 0.667
    assert report["good_event_ratio"] == 0.333


def test_rate_limit_degrades_after_capacity() -> None:
    module = load_module(
        "06_rate_limit_and_graceful_degradation.py",
        "rate_limit_module",
    )
    window = module.RateLimitWindow(allowed=1)

    first = module.handle_request(window)
    second = module.handle_request(window)

    assert first["status"] == "ok"
    assert second["status"] == "degraded"


def main() -> None:
    test_idempotency_replays_same_response()
    test_sli_report_uses_latency_and_status()
    test_rate_limit_degrades_after_capacity()
    print("test_backend_scale_patterns.py passed.")


if __name__ == "__main__":
    main()
