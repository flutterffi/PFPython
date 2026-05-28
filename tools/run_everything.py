"""Run every lesson script to verify the repository stays executable."""

from pathlib import Path
import subprocess
import sys


def iter_python_files(project_root: Path) -> list[Path]:
    directories = [
        "foundations",
        "core_python",
        "standard_library",
        "engineering",
        "advanced",
        "packaging",
        "interview",
        "projects",
        "tests",
        "modules",
        "pfpython",
    ]
    files: list[Path] = []

    for directory in directories:
        for file_path in sorted((project_root / directory).rglob("*.py")):
            if file_path.name == "__init__.py":
                continue
            files.append(file_path)

    return files


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    python_files = iter_python_files(project_root)

    failures: list[Path] = []
    for file_path in python_files:
        print(f"Running {file_path.relative_to(project_root)}")
        result = subprocess.run(
            [sys.executable, str(file_path)],
            cwd=project_root,
            check=False,
        )
        if result.returncode != 0:
            failures.append(file_path)

    if failures:
        print("\nFailures:")
        for file_path in failures:
            print(f"- {file_path.relative_to(project_root)}")
        raise SystemExit(1)

    print(f"\nSuccess: ran {len(python_files)} files.")


if __name__ == "__main__":
    main()
