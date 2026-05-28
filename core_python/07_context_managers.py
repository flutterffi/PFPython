"""Core lesson 07: context managers with a custom class."""

from pathlib import Path


class TemporaryNote:
    def __init__(self, path: Path, text: str) -> None:
        self.path = path
        self.text = text

    def __enter__(self) -> Path:
        self.path.write_text(self.text, encoding="utf-8")
        return self.path

    def __exit__(self, exc_type, exc, tb) -> bool:
        if self.path.exists():
            self.path.unlink()
        return False


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    note_path = project_root / "data" / "temporary_note.txt"

    with TemporaryNote(note_path, "Practice one small idea at a time.") as created_file:
        print(f"file exists inside context: {created_file.exists()}")
        print(created_file.read_text(encoding="utf-8"))

    print(f"file exists after context: {note_path.exists()}")


if __name__ == "__main__":
    main()
