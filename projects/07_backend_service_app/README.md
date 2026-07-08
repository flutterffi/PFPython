# Backend Service App

This project is a small multi-file backend practice app.

It is designed to feel closer to a real Python service while still staying easy to run and modify.

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

## Run Commands

```bash
python3 projects/07_backend_service_app/main.py --topic logging
python3 projects/07_backend_service_app/config.py
python3 projects/07_backend_service_app/logger.py
python3 projects/07_backend_service_app/models.py
python3 projects/07_backend_service_app/repository.py
python3 projects/07_backend_service_app/service.py
python3 projects/07_backend_service_app/routes.py
python3 tests/test_backend_service_app.py
python3 tests/test_backend_routes.py
```

## What To Practice

- swap the repository from memory to sqlite
- add request IDs into the main flow
- move the settings into environment variables
- add a second endpoint concept in `routes.py`
- write tests around the service before changing the repository
