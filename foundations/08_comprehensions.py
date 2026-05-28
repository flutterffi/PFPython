"""Lesson 08: list, dict, and set comprehensions."""


def main() -> None:
    numbers = list(range(1, 8))
    squares = [number * number for number in numbers]
    even_square_map = {number: number * number for number in numbers if number % 2 == 0}
    word_lengths = {len(word) for word in ["python", "module", "import", "loop"]}

    print(f"{numbers = }")
    print(f"{squares = }")
    print(f"{even_square_map = }")
    print(f"{word_lengths = }")


if __name__ == "__main__":
    main()
