# Packaging Track

This track follows the official package and project structure mindset.

Official base:

- [Python Packaging User Guide](https://packaging.python.org/guides/)
- [Modules Tutorial](https://docs.python.org/3/tutorial/modules.html)
- [`__main__`](https://docs.python.org/3/library/__main__.html)

## Best Repository Match

### Package Layout

Repository files:

- `packaging/01_local_package_layout.py`
- `pfpython/__init__.py`
- `pfpython/__main__.py`

### Reusable Internal Modules

Repository files:

- `pfpython/banner.py`
- `pfpython/math_utils.py`
- `pfpython/models.py`
- `pfpython/progress.py`
- `pfpython/logs.py`

### Command-Line Entry Thinking

Repository files:

- `packaging/02_entry_points_overview.py`
- `modules/03_cli_arguments.py`
- `engineering/02_small_cli_app.py`

### Multi-File Application Structure

Repository files:

- `projects/04_habit_tracker_app/`
- `projects/05_study_assistant_app/`
- `projects/06_revision_trainer_app/`

## Recommended Order

1. Learn `modules/`
2. Read `packaging/`
3. Inspect `pfpython/`
4. Inspect multi-file project folders
5. Build your own package-like mini project later
