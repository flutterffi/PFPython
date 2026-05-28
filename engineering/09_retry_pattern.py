"""Engineering lesson 09: a simple retry pattern."""

from typing import Optional


def flaky_operation(attempt: int) -> str:
    if attempt < 3:
        raise ValueError(f"attempt {attempt} failed")
    return "success"


def run_with_retry(max_attempts: int) -> str:
    last_error: Optional[Exception] = None
    for attempt in range(1, max_attempts + 1):
        try:
            return flaky_operation(attempt)
        except ValueError as error:
            print(f"retrying after: {error}")
            last_error = error
    raise RuntimeError(f"operation failed after retries: {last_error}")


def main() -> None:
    print(run_with_retry(4))


if __name__ == "__main__":
    main()
