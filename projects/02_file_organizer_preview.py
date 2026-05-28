"""Project 02: preview how files could be grouped by extension."""

from collections import defaultdict
from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    groups: dict[str, list[str]] = defaultdict(list)
    ignored_parts = {".git", ".pycache", "__pycache__"}

    for path in project_root.rglob("*"):
        if path.is_file() and ignored_parts.isdisjoint(path.parts):
            suffix = path.suffix or "<no_extension>"
            groups[suffix].append(str(path.relative_to(project_root)))

    for suffix in sorted(groups):
        print(f"\n{suffix}")
        for file_name in sorted(groups[suffix])[:5]:
            print(f"- {file_name}")


if __name__ == "__main__":
    main()
