"""Tests for practice log helpers."""

from pathlib import Path
import importlib.util


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_module(module_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_log_count_functions_exist() -> None:
    module = load_module(PROJECT_ROOT / "pfpython" / "logs.py", "logs_module")
    assert isinstance(module.count_daily_logs(), int)
    assert isinstance(module.count_weekly_logs(), int)


def test_dashboard_includes_log_counts() -> None:
    module = load_module(PROJECT_ROOT / "tools" / "progress_dashboard.py", "progress_dashboard_logs")
    dashboard = module.build_dashboard_data(PROJECT_ROOT)
    assert "daily_logs" in dashboard
    assert "weekly_logs" in dashboard


def main() -> None:
    test_log_count_functions_exist()
    test_dashboard_includes_log_counts()
    print("test_log_tools.py passed.")


if __name__ == "__main__":
    main()
