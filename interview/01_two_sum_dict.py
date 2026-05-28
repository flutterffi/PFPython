"""Interview lesson 01: solve two-sum with a dictionary."""

from typing import Optional


def two_sum(numbers: list[int], target: int) -> Optional[tuple[int, int]]:
    seen: dict[int, int] = {}
    for index, value in enumerate(numbers):
        partner = target - value
        if partner in seen:
            return seen[partner], index
        seen[value] = index
    return None


def main() -> None:
    result = two_sum([2, 7, 11, 15], 9)
    print(f"result = {result}")


if __name__ == "__main__":
    main()
