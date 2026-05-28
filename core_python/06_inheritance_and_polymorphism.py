"""Core lesson 06: inheritance and shared interfaces."""


class Exercise:
    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> str:
        return f"Exercise: {self.name}"


class SyntaxExercise(Exercise):
    def describe(self) -> str:
        return f"Syntax exercise: {self.name}"


class ProjectExercise(Exercise):
    def describe(self) -> str:
        return f"Project exercise: {self.name}"


def main() -> None:
    exercises = [
        SyntaxExercise("Practice decorators"),
        ProjectExercise("Build a CLI tracker"),
    ]

    for exercise in exercises:
        print(exercise.describe())


if __name__ == "__main__":
    main()
