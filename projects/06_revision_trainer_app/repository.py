"""Project 06 persistence helpers."""

from pathlib import Path
import json


def data_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "revision_trainer_sessions.json"


def load_sessions() -> list[dict[str, object]]:
    path = data_path()
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_sessions(items: list[dict[str, object]]) -> None:
    data_path().write_text(json.dumps(items, indent=2), encoding="utf-8")


def main() -> None:
    save_sessions([{"topic": "queues", "attempt": 1}])
    print(load_sessions())


if __name__ == "__main__":
    main()
