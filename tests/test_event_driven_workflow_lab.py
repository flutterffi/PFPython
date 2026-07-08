"""Tests for the event-driven workflow lab project."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = PROJECT_ROOT / "projects" / "09_event_driven_workflow_lab"

if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from projector import build_projection
from service import WorkflowLabService


def test_workflow_lab_publishes_events_and_projection() -> None:
    service = WorkflowLabService()
    result = service.run_workflow("payments")

    assert result["state"]["status"] in {"running", "completed"}
    assert len(result["events"]) == 3
    assert result["projection"]["event_count"] == 3


def test_workflow_lab_compensates_failed_publish() -> None:
    service = WorkflowLabService()
    result = service.run_workflow("payments", fail_step="publish")

    assert result["state"]["status"] == "compensating"
    assert any(step.startswith("compensate:") for step in result["state"]["steps"])


def test_projection_groups_events_by_topic() -> None:
    service = WorkflowLabService()
    result = service.run_workflow("orders")
    projection = build_projection(
        [
            type("Event", (), event)()  # simple attribute object for projection shape reuse
            for event in result["events"]
        ]
    )
    assert "orders" in projection["topics"]


def main() -> None:
    test_workflow_lab_publishes_events_and_projection()
    test_workflow_lab_compensates_failed_publish()
    test_projection_groups_events_by_topic()
    print("test_event_driven_workflow_lab.py passed.")


if __name__ == "__main__":
    main()
