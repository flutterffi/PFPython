"""Advanced lesson 08: memoization with lru_cache."""

from functools import lru_cache
from time import perf_counter


@lru_cache(maxsize=None)
def fibonacci_number(value: int) -> int:
    if value < 2:
        return value
    return fibonacci_number(value - 1) + fibonacci_number(value - 2)


def main() -> None:
    start = perf_counter()
    result = fibonacci_number(30)
    first_duration = perf_counter() - start

    start = perf_counter()
    cached_result = fibonacci_number(30)
    second_duration = perf_counter() - start

    print(f"first result = {result}, duration = {first_duration:.6f}s")
    print(f"cached result = {cached_result}, duration = {second_duration:.6f}s")


if __name__ == "__main__":
    main()
