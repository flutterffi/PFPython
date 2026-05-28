"""Print a simple progress dashboard for the repository."""

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


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    total = 0

    print("PFPython Progress Dashboard")
    print("==========================")

    for stage in STAGES:
        stage_path = project_root / stage
        file_count = count_python_files(stage_path)
        total += file_count
        print(f"{stage:16} {file_count:>3} runnable Python files")

    print("--------------------------")
    print(f"total            {total:>3} runnable Python files")


if __name__ == "__main__":
    main()
