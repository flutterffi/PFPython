# Folder Guide

This file explains how the repository is organized, so you can quickly choose the right place to practice.

## Main Classification

The repository is divided into 4 practical groups:

1. skill building
2. engineering and testing
3. project practice
4. planning and tracking

## 1. Skill Building

These folders are best when you want to improve language fluency.

- `foundations/`
  Best for basic syntax, control flow, functions, collections, and exceptions.

- `core_python/`
  Best for deeper language concepts such as dataclasses, decorators, protocols, and context managers.

- `standard_library/`
  Best for real built-in modules like `pathlib`, `json`, `csv`, `sqlite3`, `datetime`, and `re`.

- `advanced/`
  Best for async, queues, concurrency comparisons, caching, and worker patterns.

- `interview/`
  Best for short problem-solving drills and quick explanation practice.

## 2. Engineering And Testing

These folders are best when you want to practice project habits, not just syntax.

- `engineering/`
  Best for CLI design, logging, retry patterns, configuration, mocking, and testing habits.

- `tests/`
  Best for reading examples of direct-run tests and support checks for different parts of the repo.

- `packaging/`
  Best for understanding package layout, reusable project structure, and `python -m`.

- `modules/`
  Best for imports, package usage, and file-to-file code organization.

- `pfpython/`
  Best for reusable helper modules and the internal support layer of the repository.

## 3. Project Practice

These folders are best when you want to build things and connect multiple ideas together.

- `projects/01_todo_cli.py`
  A simple CLI-focused practice entry.

- `projects/02_file_organizer_preview.py`
  A file inspection and grouping practice entry.

- `projects/03_study_tracker_sqlite.py`
  A database-focused practice entry.

- `projects/04_habit_tracker_app/`
  A small multi-file application.

- `projects/05_study_assistant_app/`
  A config + logging + service style application.

- `projects/06_revision_trainer_app/`
  A queue and retry flavored application.

- `projects/07_backend_service_app/`
  A backend-style multi-file practice app with config, logging, service, repository, optional FastAPI routing ideas, and a package-based app skeleton.

- `special_topics/project_architecture/`
  A final advanced topic for layered design, dependency flow, bootstrap, and refactoring toward real-world structure.

- `special_topics/backend_architecture/`
  A backend-focused advanced topic for logging, FastAPI-style app structure, request flow, and service boundaries.

## 4. Planning And Tracking

These folders are best when you want structure, review, and progress visibility.

- `learning_paths/`
  Contains the 30, 60, and 90 day plans.

- `practice_system/`
  Contains templates, challenge lists, and log folders.

- `practice_system/logs/daily/`
  Your daily practice notes go here.

- `practice_system/logs/weekly/`
  Your weekly reviews go here.

- `tools/`
  Contains helper commands for suggestions, completion tracking, dashboards, and repository checks.

- `data/`
  Stores generated local practice state and small sample files.

## Best Folder Choices By Goal

If you want to:

- learn syntax fast: start with `foundations/`
- understand Python better: move to `core_python/`
- use real built-in tools: go to `standard_library/`
- build stronger habits: go to `engineering/`
- practice full exercises: go to `projects/`
- train for larger real-world structure: go to `special_topics/project_architecture/`
- train for API and backend architecture: go to `special_topics/backend_architecture/`
- review what you already learned: use `practice_system/` and `tools/`

## Suggested Daily Use

1. Pick a track from `practice_tracks/`
2. Run `tools/suggest_today.py`
3. Study one file
4. Mark it complete
5. Write a daily log
6. Check the dashboard
