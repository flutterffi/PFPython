"""Show the next suggested file for the active study plan."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.progress import load_progress
from tools.suggest_today import PLANS


def main() -> None:
    progress = load_progress()
    active_plan = str(progress["active_plan"])
    completed = set(progress["completed_files"])
    files = PLANS.get(active_plan, PLANS["30"])

    next_file = None
    for file_name in files:
        if file_name not in completed:
            next_file = file_name
            break

    print(f"Active plan: {active_plan}")
    print(f"Next file: {next_file or 'all plan files currently completed'}")


if __name__ == "__main__":
    main()
