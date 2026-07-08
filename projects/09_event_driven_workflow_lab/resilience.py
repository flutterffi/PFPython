"""Retry and circuit-breaker primitives for the event-driven workflow lab."""

from dataclasses import dataclass


@dataclass
class RetryPolicy:
    max_attempts: int


@dataclass
class CircuitBreaker:
    failure_threshold: int
    failure_count: int = 0
    state: str = "closed"

    def record_success(self) -> None:
        self.failure_count = 0
        self.state = "closed"

    def record_failure(self) -> None:
        self.failure_count += 1
        if self.failure_count >= self.failure_threshold:
            self.state = "open"

    def allow_request(self) -> bool:
        return self.state != "open"


def execute_with_retry(
    action_name: str,
    fail_times: int,
    retry_policy: RetryPolicy,
    circuit_breaker: CircuitBreaker,
) -> dict[str, object]:
    attempts = 0

    while attempts < retry_policy.max_attempts:
        if not circuit_breaker.allow_request():
            return {
                "action": action_name,
                "status": "blocked",
                "attempts": attempts,
                "breaker_state": circuit_breaker.state,
            }

        attempts += 1
        if attempts <= fail_times:
            circuit_breaker.record_failure()
            continue

        circuit_breaker.record_success()
        return {
            "action": action_name,
            "status": "succeeded",
            "attempts": attempts,
            "breaker_state": circuit_breaker.state,
        }

    return {
        "action": action_name,
        "status": "failed",
        "attempts": attempts,
        "breaker_state": circuit_breaker.state,
    }


def main() -> None:
    retry_policy = RetryPolicy(max_attempts=3)
    circuit_breaker = CircuitBreaker(failure_threshold=2)
    print("Resilience demo")
    print("=" * 15)
    print(
        execute_with_retry(
            action_name="publish-events",
            fail_times=1,
            retry_policy=retry_policy,
            circuit_breaker=circuit_breaker,
        )
    )


if __name__ == "__main__":
    main()
