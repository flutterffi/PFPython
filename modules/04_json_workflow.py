"""Module lesson 04: reading JSON and transforming data."""

import json
from pathlib import Path


def load_people() -> list[dict[str, object]]:
    project_root = Path(__file__).resolve().parents[1]
    data_file = project_root / "data" / "sample_people.json"
    return json.loads(data_file.read_text(encoding="utf-8"))


def main() -> None:
    people = load_people()
    names = [person["name"] for person in people]
    mentors = [person["name"] for person in people if person["years_of_practice"] >= 5]

    print(f"All names: {names}")
    print(f"Possible mentors: {mentors}")


if __name__ == "__main__":
    main()
