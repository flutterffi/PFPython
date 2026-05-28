"""Shared pytest-style helpers."""

from pathlib import Path
from tempfile import TemporaryDirectory
import json


def create_temp_json_file(payload: dict[str, object]) -> tuple[TemporaryDirectory, Path]:
    temp_dir = TemporaryDirectory()
    file_path = Path(temp_dir.name) / "sample.json"
    file_path.write_text(json.dumps(payload), encoding="utf-8")
    return temp_dir, file_path


def main() -> None:
    temp_dir, file_path = create_temp_json_file({"topic": "fixtures", "minutes": 15})
    try:
        print(file_path.read_text(encoding="utf-8"))
    finally:
        temp_dir.cleanup()


if __name__ == "__main__":
    main()
