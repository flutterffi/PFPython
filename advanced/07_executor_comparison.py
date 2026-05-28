"""Advanced lesson 07: compare sequential work and a thread executor."""

from concurrent.futures import ThreadPoolExecutor
from time import perf_counter


def compute_square_sum(limit: int) -> int:
    return sum(value * value for value in range(limit))


def run_sequential() -> None:
    start = perf_counter()
    results = [compute_square_sum(40_000), compute_square_sum(45_000)]
    duration = perf_counter() - start
    print(f"sequential: {duration:.4f}s -> {results}")


def run_thread_pool() -> None:
    start = perf_counter()
    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(compute_square_sum, [40_000, 45_000]))
    duration = perf_counter() - start
    print(f"thread pool: {duration:.4f}s -> {results}")


def main() -> None:
    print("This environment-friendly example avoids process pools because some sandboxes block them.")
    run_sequential()
    run_thread_pool()


if __name__ == "__main__":
    main()
