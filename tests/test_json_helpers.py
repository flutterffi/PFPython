"""Tests for fixture-style helper utilities."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.conftest import create_temp_json_file


def test_create_temp_json_file() -> None:
    temp_dir, file_path = create_temp_json_file({"topic": "json", "minutes": 10})
    try:
        assert file_path.exists()
        assert '"topic": "json"' in file_path.read_text(encoding="utf-8")
    finally:
        temp_dir.cleanup()


def main() -> None:
    test_create_temp_json_file()
    print("test_json_helpers.py passed.")


if __name__ == "__main__":
    main()
