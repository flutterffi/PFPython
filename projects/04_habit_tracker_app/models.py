"""Project 04 model objects."""

from dataclasses import dataclass


@dataclass
class HabitRecord:
    name: str
    streak: int

    def summary(self) -> str:
        return f"{self.name}: {self.streak} day streak"


def main() -> None:
    record = HabitRecord("Read Python docs", 5)
    print(record.summary())


if __name__ == "__main__":
    main()
