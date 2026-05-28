"""Tests for tools.progress_dashboard."""

from pathlib import Path
import importlib.util


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_module(module_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_collect_stage_counts_has_foundations() -> None:
    module = load_module(PROJECT_ROOT / "tools" / "progress_dashboard.py", "progress_dashboard_module")
    stage_counts = dict(module.collect_stage_counts(PROJECT_ROOT))
    assert "foundations" in stage_counts
    assert stage_counts["foundations"] >= 12


def test_build_dashboard_data_has_total() -> None:
    module = load_module(PROJECT_ROOT / "tools" / "progress_dashboard.py", "progress_dashboard_module_data")
    dashboard = module.build_dashboard_data(PROJECT_ROOT)
    assert dashboard["total_files"] >= 81
    assert len(dashboard["stages"]) >= 10


def main() -> None:
    test_collect_stage_counts_has_foundations()
    test_build_dashboard_data_has_total()
    print("test_progress_dashboard.py passed.")


if __name__ == "__main__":
    main()
