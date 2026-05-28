"""Project 04: a multi-file habit tracker application."""

from argparse import ArgumentParser
from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from models import HabitRecord
from report import build_report
from storage import load_habits, save_habits


def parse_args():
    parser = ArgumentParser(description="A small multi-file habit tracker.")
    parser.add_argument("--add", help="Add a habit name.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    items = load_habits()

    if args.add:
        items.append({"name": args.add, "streak": 1})
        save_habits(items)

    records = [HabitRecord(name=str(item["name"]), streak=int(item["streak"])) for item in items]
    print(build_report(records))


if __name__ == "__main__":
    main()
