"""Advanced lesson 02: creating a custom iterable class."""


class Countdown:
    def __init__(self, start: int) -> None:
        self.start = start

    def __iter__(self):
        current = self.start
        while current > 0:
            yield current
            current -= 1


def main() -> None:
    countdown = Countdown(5)
    print(list(countdown))


if __name__ == "__main__":
    main()
