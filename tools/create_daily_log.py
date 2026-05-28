"""Create a daily practice log from the template."""

from argparse import ArgumentParser
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.logs import daily_log_path


def parse_args():
    parser = ArgumentParser(description="Create a daily practice log file.")
    parser.add_argument("--date", help="Optional date in YYYY-MM-DD format.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    template_path = PROJECT_ROOT / "practice_system" / "daily_log_template.md"
    target_path = daily_log_path(args.date)

    if target_path.exists():
        print(f"Daily log already exists: {target_path}")
        return

    target_path.write_text(template_path.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Created daily log: {target_path}")


if __name__ == "__main__":
    main()
