"""Lesson 12: iterators and generators."""


def countdown(start: int):
    current = start
    while current > 0:
        yield current
        current -= 1


def main() -> None:
    values = list(countdown(5))
    print(f"{values = }")

    generator = countdown(3)
    print(next(generator))
    print(next(generator))
    print(next(generator))


if __name__ == "__main__":
    main()
