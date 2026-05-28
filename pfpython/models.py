"""Simple data models used by module lessons."""

from dataclasses import dataclass


@dataclass
class LearnerProfile:
    name: str
    goal: str
    study_days: int

    def summary(self) -> str:
        return f"{self.name} is practicing {self.goal} for {self.study_days} days."


def main() -> None:
    learner = LearnerProfile(name="Plato", goal="Python", study_days=30)
    print(learner.summary())


if __name__ == "__main__":
    main()
