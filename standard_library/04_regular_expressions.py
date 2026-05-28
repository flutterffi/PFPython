"""Standard library lesson 04: extracting patterns with regex."""

import re


def main() -> None:
    text = "Practice logs: lesson_01, lesson_07, project_03, note_alpha"
    lesson_matches = re.findall(r"lesson_(\d+)", text)
    replaced = re.sub(r"project_(\d+)", r"project-\1", text)

    print(f"{lesson_matches = }")
    print(f"{replaced = }")


if __name__ == "__main__":
    main()
