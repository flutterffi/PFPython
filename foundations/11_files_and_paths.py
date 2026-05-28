"""Lesson 11: reading files with pathlib."""

from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    sample_file = project_root / "data" / "sample_people.json"

    print(f"Project root: {project_root}")
    print(f"Sample file exists: {sample_file.exists()}")
    print("First 80 characters:")
    print(sample_file.read_text(encoding="utf-8")[:80])


if __name__ == "__main__":
    main()
