"""Advanced lesson 04: processing data with generator pipelines."""


def numbers(limit: int):
    for value in range(limit):
        yield value


def even_values(source):
    for value in source:
        if value % 2 == 0:
            yield value


def squared_values(source):
    for value in source:
        yield value * value


def main() -> None:
    pipeline = squared_values(even_values(numbers(10)))
    print(list(pipeline))


if __name__ == "__main__":
    main()
