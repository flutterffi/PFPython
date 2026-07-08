# Backend Service App

This project is a small multi-file backend practice app.

It is designed to feel closer to a real Python service while still staying easy to run and modify.

It now has two layers of practice:

- simple script-style files for early backend training
- a `backend_app/` package for more standard project structure

## Files

- `main.py`
  Entry point for local practice.

- `config.py`
  App settings and simple environment loading.

- `logger.py`
  Structured logging setup.

- `models.py`
  Data shapes used by the service.

- `repository.py`
  Data-access layer with an in-memory practice repository.

- `service.py`
  Business logic layer.

- `routes.py`
  Optional FastAPI-style route wiring with a safe fallback.

- `app_main.py`
  A more standard app entry file that connects the package-based structure.

- `backend_app/`
  A package-oriented backend skeleton with settings, repositories, services, bootstrap, and API wiring.

## Run Commands

```bash
python3 projects/07_backend_service_app/main.py --topic logging
python3 projects/07_backend_service_app/config.py
python3 projects/07_backend_service_app/logger.py
python3 projects/07_backend_service_app/models.py
python3 projects/07_backend_service_app/repository.py
python3 projects/07_backend_service_app/service.py
python3 projects/07_backend_service_app/routes.py
python3 projects/07_backend_service_app/app_main.py
python3 projects/07_backend_service_app/backend_app/settings.py
python3 projects/07_backend_service_app/backend_app/repositories.py
python3 projects/07_backend_service_app/backend_app/services.py
python3 projects/07_backend_service_app/backend_app/bootstrap.py
python3 projects/07_backend_service_app/backend_app/api.py
python3 tests/test_backend_service_app.py
python3 tests/test_backend_routes.py
python3 tests/test_backend_app_package.py
```

## What To Practice

- swap the repository from memory to sqlite
- add request IDs into the main flow
- move the settings into environment variables
- add a second endpoint concept in `routes.py`
- write tests around the service before changing the repository
- compare `main.py` with `app_main.py` and explain the structure difference
