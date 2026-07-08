"""Tests for the event-driven workflow lab project."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = PROJECT_ROOT / "projects" / "09_event_driven_workflow_lab"

if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from projector import build_projection, rebuild_projection
from service import WorkflowLabService


def test_workflow_lab_publishes_events_and_projection() -> None:
    service = WorkflowLabService()
    result = service.run_workflow("payments")

    assert result["state"]["status"] in {"running", "completed"}
    assert result["publish_result"]["status"] == "succeeded"
    assert len(result["events"]) == 3
    assert result["projection"]["event_count"] == 3


def test_workflow_lab_compensates_failed_publish() -> None:
    service = WorkflowLabService()
    result = service.run_workflow("payments", fail_step="publish")

    assert result["state"]["status"] == "compensating"
    assert any(step.startswith("compensate:") for step in result["state"]["steps"])


def test_workflow_lab_retries_publish_until_success() -> None:
    service = WorkflowLabService()
    result = service.run_workflow("payments", publish_fail_times=1)

    assert result["publish_result"]["status"] == "succeeded"
    assert result["publish_result"]["attempts"] == 2
    assert len(result["events"]) == 3


def test_workflow_lab_opens_circuit_after_repeated_failures() -> None:
    service = WorkflowLabService()
    result = service.run_workflow("payments", publish_fail_times=3)

    assert result["publish_result"]["status"] == "blocked"
    assert result["publish_result"]["breaker_state"] == "open"
    assert result["state"]["status"] == "compensating"


def test_workflow_lab_deduplicates_republished_events() -> None:
    service = WorkflowLabService()
    result = service.run_workflow("payments", duplicate_publish=True)

    assert len(result["events"]) == 6
    assert result["consumer_report"]["processed_count"] == 3
    assert result["consumer_report"]["duplicate_count"] == 3


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


def test_rebuilt_projection_marks_replay_state() -> None:
    service = WorkflowLabService()
    result = service.run_workflow("payments")
    rebuilt = rebuild_projection(
        [
            type("Event", (), event)()
            for event in result["events"]
        ]
    )
    assert rebuilt["rebuilt"] is True
    assert rebuilt["unique_topics"] == ["payments"]


def main() -> None:
    test_workflow_lab_publishes_events_and_projection()
    test_workflow_lab_compensates_failed_publish()
    test_workflow_lab_retries_publish_until_success()
    test_workflow_lab_opens_circuit_after_repeated_failures()
    test_workflow_lab_deduplicates_republished_events()
    test_projection_groups_events_by_topic()
    test_rebuilt_projection_marks_replay_state()
    print("test_event_driven_workflow_lab.py passed.")


if __name__ == "__main__":
    main()
