"""Core lesson 04: a simple timing decorator."""

from time import perf_counter


def measure_runtime(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        duration = perf_counter() - start
        print(f"{func.__name__} took {duration:.6f} seconds")
        return result

    return wrapper


@measure_runtime
def build_total(limit: int) -> int:
    return sum(range(limit))


def main() -> None:
    total = build_total(100_000)
    print(f"total = {total}")


if __name__ == "__main__":
    main()
