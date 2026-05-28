"""Project 04 storage helpers."""

from pathlib import Path
import json


def data_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "habit_tracker.json"


def load_habits() -> list[dict[str, object]]:
    path = data_path()
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_habits(items: list[dict[str, object]]) -> None:
    data_path().write_text(json.dumps(items, indent=2), encoding="utf-8")


def main() -> None:
    sample = [{"name": "Practice Python", "streak": 3}]
    save_habits(sample)
    print(load_habits())


if __name__ == "__main__":
    main()
