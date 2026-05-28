"""Lesson 07: lists, tuples, dictionaries, and sets."""


def main() -> None:
    languages = ["Python", "Go", "Dart"]
    coordinates = (23.1, 113.3)
    profile = {"name": "Plato", "focus": "practice", "streak": 5}
    completed_topics = {"variables", "loops", "functions", "loops"}

    languages.append("Rust")

    print(f"{languages = }")
    print(f"{coordinates = }")
    print(f"{profile['focus'] = }")
    print(f"{completed_topics = }")


if __name__ == "__main__":
    main()
