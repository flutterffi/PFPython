"""Advanced lesson 03: compare small implementations with timing."""

from time import perf_counter


def measure(label: str, func) -> None:
    start = perf_counter()
    result = func()
    duration = perf_counter() - start
    print(f"{label}: {duration:.6f}s, result={result}")


def sum_with_loop() -> int:
    total = 0
    for value in range(100_000):
        total += value
    return total


def sum_with_builtin() -> int:
    return sum(range(100_000))


def main() -> None:
    measure("loop", sum_with_loop)
    measure("builtin", sum_with_builtin)


if __name__ == "__main__":
    main()
