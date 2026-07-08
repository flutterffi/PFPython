# Backend Architecture Topic

This topic is a practical bridge from general Python practice into backend engineering.

It is meant for the stage where you already understand Python syntax, functions, modules, and small projects, and now want to practice how backend systems are shaped.

Use this topic to practice:

- separating API, service, and repository responsibilities
- adding structured logging to backend code
- understanding FastAPI-style app layout
- tracing a request from input to response
- preparing your own later backend exercises

## Run Order

Start with these files in order:

1. `python3 special_topics/backend_architecture/01_backend_layers.py`
2. `python3 special_topics/backend_architecture/02_structured_logging.py`
3. `python3 special_topics/backend_architecture/03_fastapi_app_structure.py`
4. `python3 special_topics/backend_architecture/04_request_lifecycle.py`

## What You Should Practice

After running each file, try one or more of these exercises:

- replace in-memory data with a file or sqlite repository
- add a request ID and pass it through logs
- split one backend example into more modules
- add a new API endpoint concept and describe its service logic
- turn printed responses into JSON dictionaries
- compare CLI architecture and API architecture

## Core Backend Mental Model

When a backend project grows, try this model:

1. schema or contract: what comes in and out
2. router or controller: how requests enter
3. service: where business rules live
4. repository: where data access lives
5. infrastructure: logging, config, database, and startup wiring

## Official Study Links

Use these while training:

- [FastAPI docs](https://fastapi.tiangolo.com/)
- [FastAPI bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [Uvicorn docs](https://www.uvicorn.org/)
- [Pydantic docs](https://pydantic.dev/docs/validation/latest/get-started/)
- [Python logging docs](https://docs.python.org/3/library/logging.html)

## Good Refactor Targets In This Repository

These files are strong candidates for backend-style refactors later:

- `projects/03_study_tracker_sqlite.py`
- `projects/05_study_assistant_app/main.py`
- `projects/06_revision_trainer_app/main.py`

## Important Note

The FastAPI lesson in this topic is safe to run even if `fastapi` is not installed locally.

If the dependency is missing, the file will still teach the intended architecture and show the next installation step.
