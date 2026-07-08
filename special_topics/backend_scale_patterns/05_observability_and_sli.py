"""Practice observability signals and a simple SLI calculation."""

from dataclasses import dataclass


@dataclass
class RequestSample:
    latency_ms: int
    status_code: int


def calculate_sli(samples: list[RequestSample], latency_budget_ms: int) -> dict[str, object]:
    total = len(samples)
    good = [
        sample
        for sample in samples
        if sample.status_code < 500 and sample.latency_ms <= latency_budget_ms
    ]
    availability = round(len([s for s in samples if s.status_code < 500]) / total, 3)
    good_ratio = round(len(good) / total, 3)
    return {
        "total_requests": total,
        "availability_sli": availability,
        "good_event_ratio": good_ratio,
        "latency_budget_ms": latency_budget_ms,
    }


def main() -> None:
    samples = [
        RequestSample(latency_ms=80, status_code=200),
        RequestSample(latency_ms=120, status_code=200),
        RequestSample(latency_ms=250, status_code=503),
        RequestSample(latency_ms=95, status_code=200),
        RequestSample(latency_ms=170, status_code=200),
    ]
    report = calculate_sli(samples, latency_budget_ms=150)

    print("Observability and SLI")
    print("=" * 21)
    print(report)
    print("\nHigh-level questions:")
    print("- what should be a log, a metric, or a trace")
    print("- which SLI actually reflects user pain")
    print("- what alerts are useful without causing noise")


if __name__ == "__main__":
    main()
