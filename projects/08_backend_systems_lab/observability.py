"""Observability helpers for the backend systems lab."""


def build_snapshot(latency_ms: int, cache_hit: bool, job_count: int) -> dict[str, object]:
    return {
        "latency_ms": latency_ms,
        "cache_hit": cache_hit,
        "scheduled_jobs": job_count,
        "trace_hint": "request -> auth -> idempotency -> cache -> service -> job",
    }


def main() -> None:
    print("Observability lab demo")
    print("=" * 22)
    print(build_snapshot(latency_ms=42, cache_hit=True, job_count=1))


if __name__ == "__main__":
    main()
