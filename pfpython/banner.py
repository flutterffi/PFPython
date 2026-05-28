"""Small banner utilities for practice scripts."""


def build_banner(title: str) -> str:
    line = "=" * len(title)
    return f"{line}\n{title}\n{line}"


def main() -> None:
    print(build_banner("Practice Time"))


if __name__ == "__main__":
    main()
