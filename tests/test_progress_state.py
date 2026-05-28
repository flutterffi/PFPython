"""Tests for learner progress state helpers."""

from pathlib import Path
import importlib.util


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_module(module_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_default_progress_data_shape() -> None:
    module = load_module(PROJECT_ROOT / "pfpython" / "progress.py", "progress_module")
    progress = module.default_progress_data()
    assert progress["active_plan"] == "30"
    assert progress["completed_files"] == []


def test_dashboard_data_includes_completion() -> None:
    module = load_module(PROJECT_ROOT / "tools" / "progress_dashboard.py", "progress_dashboard_completion")
    dashboard = module.build_dashboard_data(PROJECT_ROOT)
    assert "completed_files" in dashboard
    assert "completion_percent" in dashboard


def main() -> None:
    test_default_progress_data_shape()
    test_dashboard_data_includes_completion()
    print("test_progress_state.py passed.")


if __name__ == "__main__":
    main()
