"""Project 04 reporting helpers."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from models import HabitRecord


def build_report(items: list[HabitRecord]) -> str:
    lines = ["Habit Tracker Report"]
    lines.extend(record.summary() for record in items)
    return "\n".join(lines)


def main() -> None:
    report = build_report([HabitRecord("Finish one lesson", 4)])
    print(report)


if __name__ == "__main__":
    main()
