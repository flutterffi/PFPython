"""Project 05 configuration helpers."""

from os import getenv


def load_config() -> dict[str, object]:
    return {
        "mode": getenv("PFPYTHON_ASSISTANT_MODE", "practice"),
        "default_minutes": int(getenv("PFPYTHON_ASSISTANT_MINUTES", "25")),
    }


def main() -> None:
    print(load_config())


if __name__ == "__main__":
    main()
