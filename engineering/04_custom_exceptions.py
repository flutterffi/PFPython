"""Engineering lesson 04: designing a custom exception."""


class PracticePlanError(Exception):
    """Raised when a practice plan is invalid."""


def validate_minutes(minutes: int) -> None:
    if minutes <= 0:
        raise PracticePlanError("Practice minutes must be greater than zero.")


def main() -> None:
    values = [25, 0]
    for minutes in values:
        try:
            validate_minutes(minutes)
        except PracticePlanError as error:
            print(f"Invalid plan for {minutes} minutes: {error}")
        else:
            print(f"Plan accepted for {minutes} minutes.")


if __name__ == "__main__":
    main()
