"""Lesson 10: try, except, else, and finally."""


def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b


def main() -> None:
    pairs = [(10, 2), (7, 0)]

    for left, right in pairs:
        try:
            result = safe_divide(left, right)
        except ValueError as error:
            print(f"Could not divide {left} by {right}: {error}")
        else:
            print(f"{left} / {right} = {result}")
        finally:
            print("Attempt finished.")


if __name__ == "__main__":
    main()
