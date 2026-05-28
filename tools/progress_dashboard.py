"""Print a progress dashboard for the repository."""

from argparse import ArgumentParser
import json
from pathlib import Path


STAGES = [
    "foundations",
    "core_python",
    "standard_library",
    "engineering",
    "advanced",
    "packaging",
    "interview",
    "projects",
    "tests",
    "modules",
    "pfpython",
]


def count_python_files(stage_path: Path) -> int:
    count = 0
    for file_path in stage_path.rglob("*.py"):
        if file_path.name != "__init__.py":
            count += 1
    return count


def collect_stage_counts(project_root: Path) -> list[tuple[str, int]]:
    return [(stage, count_python_files(project_root / stage)) for stage in STAGES]


def build_dashboard_data(project_root: Path) -> dict[str, object]:
    stages = collect_stage_counts(project_root)
    total = sum(file_count for _, file_count in stages)
    stage_rows = []

    for stage, file_count in stages:
        percent = 0.0 if total == 0 else (file_count / total) * 100
        stage_rows.append(
            {
                "stage": stage,
                "files": file_count,
                "percent": round(percent, 2),
            }
        )

    return {
        "total_files": total,
        "stage_count": len(stage_rows),
        "stages": stage_rows,
    }


def parse_args():
    parser = ArgumentParser(description="Show a progress dashboard for the practice repository.")
    parser.add_argument("--json", action="store_true", help="Print the dashboard as JSON.")
    parser.add_argument("--summary-only", action="store_true", help="Print only the total file count.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    project_root = Path(__file__).resolve().parents[1]
    dashboard = build_dashboard_data(project_root)

    if args.json:
        print(json.dumps(dashboard, indent=2))
        return

    if args.summary_only:
        print(f"total runnable Python files: {dashboard['total_files']}")
        return

    print("PFPython Progress Dashboard")
    print("==========================")

    for row in dashboard["stages"]:
        stage = row["stage"]
        file_count = row["files"]
        percent = row["percent"]
        print(f"{stage:16} {file_count:>3} runnable Python files ({percent:>5.2f}%)")

    print("--------------------------")
    print(f"total            {dashboard['total_files']:>3} runnable Python files")


if __name__ == "__main__":
    main()
