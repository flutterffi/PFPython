"""Lesson 02: variables, reassignment, and basic built-in types."""


def main() -> None:
    learner_name = "Plato"
    lessons_completed = 3
    confidence_score = 7.5
    is_studying_today = True

    print(f"{learner_name = }")
    print(f"{lessons_completed = }")
    print(f"{confidence_score = }")
    print(f"{is_studying_today = }")

    lessons_completed += 1
    confidence_score += 0.5

    print("After one more lesson:")
    print(f"{lessons_completed = }")
    print(f"{confidence_score = }")


if __name__ == "__main__":
    main()
