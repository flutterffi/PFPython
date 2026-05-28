"""Core lesson 01: scope, rebinding, and mutable objects."""


def rebind_number(value: int) -> int:
    value += 10
    return value


def mutate_list(values: list[int]) -> None:
    values.append(99)


def main() -> None:
    number = 5
    changed_number = rebind_number(number)
    print(f"original number: {number}")
    print(f"returned number: {changed_number}")

    items = [1, 2, 3]
    mutate_list(items)
    print(f"mutated list: {items}")

    outer_message = "Python"

    def inner() -> str:
        return f"Inner sees: {outer_message}"

    print(inner())


if __name__ == "__main__":
    main()
