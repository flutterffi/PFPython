"""Tests for tools.suggest_today."""

from pathlib import Path
import importlib.util


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_module(module_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_build_recommendation_has_project_and_challenge() -> None:
    module = load_module(PROJECT_ROOT / "tools" / "suggest_today.py", "suggest_today_module")
    recommendation = module.build_recommendation("30")
    assert recommendation["project_file"] == "projects/01_todo_cli.py"
    assert recommendation["challenge"]


def test_build_recommendation_has_plan_files() -> None:
    module = load_module(PROJECT_ROOT / "tools" / "suggest_today.py", "suggest_today_module_plan")
    recommendation = module.build_recommendation("60")
    assert len(recommendation["plan_files"]) >= 3
    assert recommendation["plan"] == "60"


def main() -> None:
    test_build_recommendation_has_project_and_challenge()
    test_build_recommendation_has_plan_files()
    print("test_suggest_today.py passed.")


if __name__ == "__main__":
    main()
