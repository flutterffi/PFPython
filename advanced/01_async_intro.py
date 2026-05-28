"""Advanced lesson 01: a minimal asyncio workflow."""

import asyncio


async def fetch_mock_result(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} finished after {delay} seconds"


async def async_main() -> None:
    results = await asyncio.gather(
        fetch_mock_result("lesson-a", 0.1),
        fetch_mock_result("lesson-b", 0.2),
    )
    for result in results:
        print(result)


def main() -> None:
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
