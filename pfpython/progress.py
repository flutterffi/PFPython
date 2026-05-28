"""Helpers for learner progress tracking."""

from datetime import date
import json
from pathlib import Path
from typing import Optional


DEFAULT_PLAN = "30"


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def progress_path() -> Path:
    return project_root() / "data" / "learner_progress.json"


def default_progress_data() -> dict[str, object]:
    return {
        "active_plan": DEFAULT_PLAN,
        "completed_files": [],
        "study_log": [],
        "notes": [],
    }


def load_progress() -> dict[str, object]:
    path = progress_path()
    if not path.exists():
        return default_progress_data()
    return json.loads(path.read_text(encoding="utf-8"))


def save_progress(progress: dict[str, object]) -> None:
    progress_path().write_text(json.dumps(progress, indent=2), encoding="utf-8")


def set_active_plan(plan: str) -> dict[str, object]:
    progress = load_progress()
    progress["active_plan"] = plan
    save_progress(progress)
    return progress


def mark_file_complete(file_name: str) -> dict[str, object]:
    progress = load_progress()
    completed_files = list(progress["completed_files"])
    if file_name not in completed_files:
        completed_files.append(file_name)
        completed_files.sort()
        progress["completed_files"] = completed_files

    study_log = list(progress["study_log"])
    study_log.append({"file": file_name, "date": date.today().isoformat()})
    progress["study_log"] = study_log
    save_progress(progress)
    return progress


def completed_file_set(progress: dict[str, object]) -> set[str]:
    return set(progress["completed_files"])


def latest_completed_file(progress: dict[str, object]) -> Optional[str]:
    study_log = progress["study_log"]
    if not study_log:
        return None
    return study_log[-1]["file"]


def recently_completed_files(progress: dict[str, object], limit: int = 3) -> list[str]:
    study_log = list(progress["study_log"])
    recent_files: list[str] = []

    for item in reversed(study_log):
        file_name = item["file"]
        if file_name not in recent_files:
            recent_files.append(file_name)
        if len(recent_files) >= limit:
            break

    return recent_files


def main() -> None:
    print(load_progress())


if __name__ == "__main__":
    main()
