# Backend Systems Lab

This project is a high-level backend practice lab.

It combines several production-style concerns in one place:

- auth scope checks
- cache-aside reads
- idempotency protection
- background job scheduling
- observability snapshots

## Files

- `main.py`
  Main lab flow that runs the whole pipeline.

- `models.py`
  Shared request and response models.

- `auth.py`
  Scope-based authorization checks.

- `cache_layer.py`
  Cache-aside simulation.

- `idempotency.py`
  Duplicate request protection.

- `jobs.py`
  Background job and dead-letter simulation.

- `observability.py`
  Metrics and trace-like summaries.

- `service.py`
  The orchestration layer that combines everything.

## Run Commands

```bash
python3 projects/08_backend_systems_lab/main.py --topic observability
python3 projects/08_backend_systems_lab/models.py
python3 projects/08_backend_systems_lab/auth.py
python3 projects/08_backend_systems_lab/cache_layer.py
python3 projects/08_backend_systems_lab/idempotency.py
python3 projects/08_backend_systems_lab/jobs.py
python3 projects/08_backend_systems_lab/observability.py
python3 projects/08_backend_systems_lab/service.py
python3 tests/test_backend_systems_lab.py
```

## High-Level Practice Ideas

- replace the in-memory cache with a redis-shaped abstraction
- add a stronger idempotency payload check
- separate write jobs from read requests
- add alert-friendly latency buckets
- design what should happen during partial cache or job failure
