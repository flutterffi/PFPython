"""Create a weekly review log from the template."""

from argparse import ArgumentParser
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.logs import weekly_log_path


def parse_args():
    parser = ArgumentParser(description="Create a weekly review log file.")
    parser.add_argument("--week", required=True, help="Week label, for example week-01.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    template_path = PROJECT_ROOT / "practice_system" / "weekly_review_template.md"
    target_path = weekly_log_path(args.week)

    if target_path.exists():
        print(f"Weekly log already exists: {target_path}")
        return

    target_path.write_text(template_path.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Created weekly log: {target_path}")


if __name__ == "__main__":
    main()
