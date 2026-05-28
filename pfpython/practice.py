"""Practice plan helpers."""


def build_practice_plan() -> list[str]:
    return [
        "Run one foundation lesson.",
        "Change one variable and predict the new output.",
        "Write one new helper function.",
        "Import that helper in another file.",
    ]


def main() -> None:
    for step in build_practice_plan():
        print(step)


if __name__ == "__main__":
    main()
