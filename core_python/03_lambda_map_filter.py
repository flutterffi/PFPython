"""Core lesson 03: lambdas, map, and filter."""


def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6]
    squared = list(map(lambda value: value * value, numbers))
    even_numbers = list(filter(lambda value: value % 2 == 0, numbers))
    combined = list(map(lambda pair: pair[0] + pair[1], zip(numbers, squared)))

    print(f"{numbers = }")
    print(f"{squared = }")
    print(f"{even_numbers = }")
    print(f"{combined = }")


if __name__ == "__main__":
    main()
