"""Advanced lesson 05: a tiny descriptor for positive integers."""


class PositiveInteger:
    def __set_name__(self, owner, name) -> None:
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value: int) -> None:
        if value <= 0:
            raise ValueError("value must be positive")
        setattr(instance, self.private_name, value)


class Session:
    minutes = PositiveInteger()

    def __init__(self, minutes: int) -> None:
        self.minutes = minutes


def main() -> None:
    session = Session(30)
    print(f"minutes = {session.minutes}")

    try:
        session.minutes = -1
    except ValueError as error:
        print(f"descriptor blocked invalid value: {error}")


if __name__ == "__main__":
    main()
