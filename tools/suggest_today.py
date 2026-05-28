"""Suggest a small daily practice plan from the repository."""

from argparse import ArgumentParser
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pfpython.progress import load_progress, set_active_plan


PLANS: dict[str, list[str]] = {
    "30": [
        "foundations/01_hello_world.py",
        "foundations/05_loops.py",
        "core_python/01_scope_and_mutability.py",
        "modules/01_imports_and_helpers.py",
        "engineering/01_pytest_basics.py",
        "projects/01_todo_cli.py",
    ],
    "60": [
        "foundations/09_classes.py",
        "core_python/05_dataclasses.py",
        "standard_library/05_sqlite_basics.py",
        "engineering/06_logging_basics.py",
        "advanced/04_generator_pipeline.py",
        "projects/04_habit_tracker_app/main.py",
    ],
    "90": [
        "engineering/08_unittest_basics.py",
        "advanced/08_lru_cache_demo.py",
        "advanced/09_queue_worker.py",
        "interview/01_two_sum_dict.py",
        "projects/05_study_assistant_app/main.py",
        "projects/06_revision_trainer_app/main.py",
    ],
}


def parse_args():
    parser = ArgumentParser(description="Suggest a short daily practice plan.")
    parser.add_argument("--plan", choices=sorted(PLANS), default="30", help="Study path length to target.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    set_active_plan(args.plan)
    progress = load_progress()
    completed = set(progress["completed_files"])
    files = PLANS[args.plan]
    new_files = [file_name for file_name in files if file_name not in completed]
    review_files = [file_name for file_name in files if file_name in completed]

    print(f"Today's practice plan for the {args.plan}-day path:")
    for index, file_name in enumerate(files, start=1):
        print(f"{index}. {file_name}")

    if new_files:
        print("\nRecommended next new file:")
        print(f"- {new_files[0]}")

    if review_files:
        print("\nRecommended review file:")
        print(f"- {review_files[-1]}")

    print("\nSuggested loop:")
    print("1. Run the file.")
    print("2. Predict the output before changing anything.")
    print("3. Modify one small part.")
    print("4. Run it again.")
    print("5. Write one note in practice_system/daily_log_template.md.")


if __name__ == "__main__":
    main()
