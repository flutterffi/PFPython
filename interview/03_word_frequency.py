"""Interview lesson 03: count words and sort results."""

from collections import Counter


def frequency_report(text: str) -> list[tuple[str, int]]:
    words = text.lower().split()
    counts = Counter(words)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))


def main() -> None:
    report = frequency_report("python practice python loops functions loops python")
    print(report)


if __name__ == "__main__":
    main()
