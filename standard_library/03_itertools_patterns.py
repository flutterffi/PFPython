"""Standard library lesson 03: small itertools patterns."""

from itertools import combinations, cycle, islice


def main() -> None:
    lesson_names = ["variables", "functions", "classes"]
    pairs = list(combinations(lesson_names, 2))
    repeated = list(islice(cycle(["A", "B", "C"]), 7))

    print(f"{pairs = }")
    print(f"{repeated = }")


if __name__ == "__main__":
    main()
