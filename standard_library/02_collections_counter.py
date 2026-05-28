"""Standard library lesson 02: counting repeated values."""

from collections import Counter


def main() -> None:
    topics = ["loops", "functions", "loops", "classes", "functions", "loops"]
    counts = Counter(topics)
    most_common = counts.most_common(2)

    print(f"{counts = }")
    print(f"{most_common = }")


if __name__ == "__main__":
    main()
