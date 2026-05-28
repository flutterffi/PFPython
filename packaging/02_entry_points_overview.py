"""Packaging lesson 02: explain entry-point style execution."""


def build_notes() -> list[str]:
    return [
        "A package can expose code through python -m package_name.",
        "A pyproject file can describe project metadata.",
        "Entry points are a common way to create CLI commands.",
    ]


def main() -> None:
    for note in build_notes():
        print(note)


if __name__ == "__main__":
    main()
