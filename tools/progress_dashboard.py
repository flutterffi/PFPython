"""Print a progress dashboard for the repository."""

from argparse import ArgumentParser
import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.logs import count_daily_logs, count_weekly_logs
from pfpython.progress import completed_file_set, latest_completed_file, load_progress


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
    progress = load_progress()
    completed_files = completed_file_set(progress)
    completed_total = 0

    for stage, file_count in stages:
        stage_path = project_root / stage
        stage_completed = 0
        for file_path in stage_path.rglob("*.py"):
            if file_path.name == "__init__.py":
                continue
            relative_path = str(file_path.relative_to(project_root))
            if relative_path in completed_files:
                stage_completed += 1

        percent = 0.0 if total == 0 else (file_count / total) * 100
        completed_percent = 0.0 if file_count == 0 else (stage_completed / file_count) * 100
        completed_total += stage_completed
        stage_rows.append(
            {
                "stage": stage,
                "files": file_count,
                "percent": round(percent, 2),
                "completed_files": stage_completed,
                "completed_percent": round(completed_percent, 2),
            }
        )

    return {
        "active_plan": progress["active_plan"],
        "total_files": total,
        "completed_files": completed_total,
        "completion_percent": round(0.0 if total == 0 else (completed_total / total) * 100, 2),
        "latest_completed_file": latest_completed_file(progress),
        "daily_logs": count_daily_logs(),
        "weekly_logs": count_weekly_logs(),
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
        completed_files = row["completed_files"]
        completed_percent = row["completed_percent"]
        print(
            f"{stage:16} {file_count:>3} files ({percent:>5.2f}%) | "
            f"completed {completed_files:>3} ({completed_percent:>5.2f}%)"
        )

    print("--------------------------")
    print(f"active plan       {dashboard['active_plan']}")
    print(f"total files      {dashboard['total_files']:>3}")
    print(f"completed files  {dashboard['completed_files']:>3} ({dashboard['completion_percent']:>5.2f}%)")
    print(f"latest completed {dashboard['latest_completed_file'] or 'none'}")
    print(f"daily logs       {dashboard['daily_logs']:>3}")
    print(f"weekly logs      {dashboard['weekly_logs']:>3}")


if __name__ == "__main__":
    main()
