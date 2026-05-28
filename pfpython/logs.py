"""Helpers for practice log files."""

from datetime import date
from pathlib import Path
from typing import Optional


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def practice_system_root() -> Path:
    return project_root() / "practice_system"


def daily_logs_dir() -> Path:
    return practice_system_root() / "logs" / "daily"


def weekly_logs_dir() -> Path:
    return practice_system_root() / "logs" / "weekly"


def ensure_log_directories() -> None:
    daily_logs_dir().mkdir(parents=True, exist_ok=True)
    weekly_logs_dir().mkdir(parents=True, exist_ok=True)


def daily_log_path(for_date: Optional[str] = None) -> Path:
    ensure_log_directories()
    suffix = for_date or date.today().isoformat()
    return daily_logs_dir() / f"{suffix}.md"


def weekly_log_path(week_name: str) -> Path:
    ensure_log_directories()
    return weekly_logs_dir() / f"{week_name}.md"


def count_daily_logs() -> int:
    ensure_log_directories()
    return len([path for path in daily_logs_dir().glob("*.md") if path.name != ".gitkeep"])


def count_weekly_logs() -> int:
    ensure_log_directories()
    return len([path for path in weekly_logs_dir().glob("*.md") if path.name != ".gitkeep"])


def main() -> None:
    ensure_log_directories()
    print(f"daily logs: {count_daily_logs()}")
    print(f"weekly logs: {count_weekly_logs()}")


if __name__ == "__main__":
    main()
