"""Saga-style workflow transitions for the event-driven workflow lab."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from models import WorkflowState


def advance_workflow(state: WorkflowState, next_step: str) -> WorkflowState:
    return WorkflowState(
        workflow_id=state.workflow_id,
        topic=state.topic,
        status="running" if next_step != "completed" else "completed",
        steps=[*state.steps, next_step],
    )


def compensate_workflow(state: WorkflowState, failed_step: str) -> WorkflowState:
    return WorkflowState(
        workflow_id=state.workflow_id,
        topic=state.topic,
        status="compensating",
        steps=[*state.steps, f"compensate:{failed_step}"],
    )


def main() -> None:
    state = WorkflowState("wf-1", "payments", "started", ["requested"])
    advanced = advance_workflow(state, "authorized")
    compensated = compensate_workflow(advanced, "capture")
    print("Saga demo")
    print("=" * 9)
    print(advanced.to_dict())
    print(compensated.to_dict())


if __name__ == "__main__":
    main()
