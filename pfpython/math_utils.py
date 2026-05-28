"""Small math helpers for tests and practice."""


def fibonacci(length: int) -> list[int]:
    if length <= 0:
        return []
    if length == 1:
        return [0]

    values = [0, 1]
    while len(values) < length:
        values.append(values[-1] + values[-2])
    return values


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, int(value ** 0.5) + 1):
        if value % divisor == 0:
            return False
    return True


def main() -> None:
    print(fibonacci(7))
    print(is_prime(13))


if __name__ == "__main__":
    main()
