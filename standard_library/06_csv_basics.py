"""Standard library lesson 06: reading and writing CSV files."""

import csv
from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "data" / "study_plan.csv"

    rows = [
        ["topic", "minutes"],
        ["loops", "20"],
        ["classes", "30"],
        ["testing", "25"],
    ]

    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    with csv_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['topic']} -> {row['minutes']} minutes")


if __name__ == "__main__":
    main()
