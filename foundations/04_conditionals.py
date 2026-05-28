"""Lesson 04: if, elif, else, and boolean logic."""


def describe_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 75:
        return "strong"
    if score >= 60:
        return "steady"
    return "keep practicing"


def main() -> None:
    scores = [95, 82, 67, 41]

    for score in scores:
        result = describe_score(score)
        passed = score >= 60
        print(f"score={score}, result={result}, passed={passed}")


if __name__ == "__main__":
    main()
