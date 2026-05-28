"""Project 05 service helpers."""

from pathlib import Path
import json

CURRENT_DIR = Path(__file__).resolve().parent


def report_path() -> Path:
    return CURRENT_DIR.parents[1] / "data" / "study_assistant_report.json"


def build_session(topic: str, minutes: int, mode: str) -> dict[str, object]:
    return {
        "topic": topic,
        "minutes": minutes,
        "mode": mode,
        "message": f"Study {topic} for {minutes} focused minutes.",
    }


def save_session(session: dict[str, object]) -> None:
    report_path().write_text(json.dumps(session, indent=2), encoding="utf-8")


def main() -> None:
    session = build_session("logging", 20, "practice")
    save_session(session)
    print(report_path().read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
