"""Advanced lesson 06: compare threading and asyncio for tiny waits."""

import asyncio
from threading import Thread
from time import perf_counter, sleep


def blocking_task(label: str, delay: float, output: list[str]) -> None:
    sleep(delay)
    output.append(f"{label} finished")


async def async_task(label: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{label} finished"


def run_threads() -> None:
    output: list[str] = []
    threads = [
        Thread(target=blocking_task, args=("thread-a", 0.1, output)),
        Thread(target=blocking_task, args=("thread-b", 0.2, output)),
    ]
    start = perf_counter()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    duration = perf_counter() - start
    print(f"threads: {duration:.4f}s -> {sorted(output)}")


async def run_async() -> None:
    start = perf_counter()
    results = await asyncio.gather(
        async_task("async-a", 0.1),
        async_task("async-b", 0.2),
    )
    duration = perf_counter() - start
    print(f"asyncio: {duration:.4f}s -> {sorted(results)}")


def main() -> None:
    run_threads()
    asyncio.run(run_async())


if __name__ == "__main__":
    main()
