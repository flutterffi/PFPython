"""Project 06 configuration helpers."""

from os import getenv


def load_config() -> dict[str, object]:
    return {
        "max_attempts": int(getenv("PFPYTHON_REVISION_ATTEMPTS", "3")),
        "worker_name": getenv("PFPYTHON_REVISION_WORKER", "trainer-worker"),
    }


def main() -> None:
    print(load_config())


if __name__ == "__main__":
    main()
