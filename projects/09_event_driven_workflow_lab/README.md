# Event Driven Workflow Lab

This project is a high-level event-driven backend lab.

It is meant for practicing workflow orchestration when one request turns into multiple asynchronous side effects.

## Files

- `main.py`
  Runs the full workflow demo.

- `models.py`
  Shared event and workflow state models.

- `outbox.py`
  Simulates the outbox pattern.

- `broker.py`
  Simulates a message broker publish and consume flow.

- `projector.py`
  Builds a read-model style projection from emitted events.

- `saga.py`
  Simulates workflow state transitions and compensation.

- `service.py`
  Coordinates the full workflow.

## Run Commands

```bash
python3 projects/09_event_driven_workflow_lab/main.py --topic payments
python3 projects/09_event_driven_workflow_lab/models.py
python3 projects/09_event_driven_workflow_lab/outbox.py
python3 projects/09_event_driven_workflow_lab/broker.py
python3 projects/09_event_driven_workflow_lab/projector.py
python3 projects/09_event_driven_workflow_lab/saga.py
python3 projects/09_event_driven_workflow_lab/service.py
python3 tests/test_event_driven_workflow_lab.py
```

## High-Level Practice Ideas

- model a duplicate publish and decide how consumers should react
- add a failed step and trigger compensation flow
- split command-side state from read-side projection more clearly
- compare synchronous response needs vs eventual consistency
- add replay support for rebuilding projections
