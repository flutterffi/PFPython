# Project Architecture Topic

This topic is the final advanced stage in PFPython.

It is designed for the moment when basic syntax is no longer the main problem, and the next challenge becomes structure.

Use this topic to practice:

- turning a single-file script into a multi-layer project
- separating domain logic from persistence and presentation
- understanding service, repository, and app bootstrap roles
- keeping dependencies flowing in one clean direction
- preparing your own future practice projects for larger growth

## Run Order

Start with these files in order:

1. `python3 special_topics/project_architecture/01_layered_architecture.py`
2. `python3 special_topics/project_architecture/02_dependency_flow.py`
3. `python3 special_topics/project_architecture/03_bootstrap_and_entrypoint.py`

## What You Should Practice

After running each file, try one or more of these exercises:

- rename classes and explain their responsibility
- move one function to a better layer
- add a new persistence implementation
- replace printed output with a CLI or web-style boundary
- extract repeated setup code into a bootstrap function
- rewrite a small project from `projects/` using the same structure

## Recommended Refactor Targets

These are good places in this repository to revisit after this topic:

- `projects/01_todo_cli.py`
- `projects/03_study_tracker_sqlite.py`
- `projects/04_habit_tracker_app/main.py`
- `projects/05_study_assistant_app/main.py`
- `projects/06_revision_trainer_app/main.py`

## Structure Thinking

When a practice project grows, try this mental model:

1. domain: what the app means
2. service: what the app does
3. repository: where data comes from or goes
4. interface: how users or other systems talk to it
5. bootstrap: how the whole app is wired together

This topic is not tied to one framework.

The goal is to build habits that still help when you later move into:

- Flask or FastAPI
- desktop tools
- larger CLI applications
- worker services
- package-based internal tools
