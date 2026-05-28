"""Packaging lesson 01: understand a simple local package layout."""

from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    package_dir = project_root / "pfpython"

    print(f"package exists: {package_dir.exists()}")
    print("Package files:")
    for path in sorted(package_dir.glob("*.py")):
        print(f"- {path.name}")


if __name__ == "__main__":
    main()
