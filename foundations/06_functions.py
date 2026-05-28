"""Lesson 06: defining functions and using return values."""


def greet(name: str) -> str:
    return f"Hello, {name}."


def multiply(a: int, b: int) -> int:
    return a * b


def summarize_progress(name: str, lessons: int) -> str:
    return f"{name} has completed {lessons} lessons."


def main() -> None:
    print(greet("Learner"))
    print(f"6 * 7 = {multiply(6, 7)}")
    print(summarize_progress("Plato", 12))


if __name__ == "__main__":
    main()
