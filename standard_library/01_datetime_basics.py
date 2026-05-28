"""Standard library lesson 01: dates, times, and durations."""

from datetime import datetime, timedelta


def main() -> None:
    started_at = datetime(2026, 5, 28, 9, 0, 0)
    study_length = timedelta(minutes=95)
    finished_at = started_at + study_length

    print(f"started_at = {started_at.isoformat()}")
    print(f"finished_at = {finished_at.isoformat()}")
    print(f"duration in minutes = {study_length.total_seconds() / 60}")


if __name__ == "__main__":
    main()
