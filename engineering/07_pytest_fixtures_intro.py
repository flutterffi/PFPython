"""Engineering lesson 07: fixture-style setup thinking."""

from pathlib import Path
from tempfile import TemporaryDirectory
import json


def make_temp_plan() -> tuple[TemporaryDirectory, Path]:
    temp_dir = TemporaryDirectory()
    plan_path = Path(temp_dir.name) / "plan.json"
    plan_path.write_text(json.dumps({"topic": "fixtures", "minutes": 20}), encoding="utf-8")
    return temp_dir, plan_path


def main() -> None:
    temp_dir, plan_path = make_temp_plan()
    try:
        print(plan_path.read_text(encoding="utf-8"))
        print("This setup function can later become a real pytest fixture.")
    finally:
        temp_dir.cleanup()


if __name__ == "__main__":
    main()
