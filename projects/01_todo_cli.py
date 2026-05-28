"""Project 01: a tiny todo CLI backed by a JSON file."""

from argparse import ArgumentParser
import json
from pathlib import Path


def data_path() -> Path:
    return Path(__file__).resolve().parents[1] / "data" / "todo_items.json"


def load_items() -> list[str]:
    path = data_path()
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_items(items: list[str]) -> None:
    data_path().write_text(json.dumps(items, indent=2), encoding="utf-8")


def parse_args():
    parser = ArgumentParser(description="A tiny practice todo CLI.")
    parser.add_argument("--add", help="Add a new todo item.")
    parser.add_argument("--clear", action="store_true", help="Remove all todo items.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    items = load_items()

    if args.clear:
        items = []
        save_items(items)
        print("Cleared all todo items.")
        return

    if args.add:
        items.append(args.add)
        save_items(items)
        print(f"Added: {args.add}")

    print("Current items:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")


if __name__ == "__main__":
    main()
