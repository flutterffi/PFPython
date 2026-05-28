"""Lesson 03: string methods, formatting, and number operators."""


def main() -> None:
    topic = "python syntax"
    print(topic.title())
    print(topic.replace("syntax", "practice"))

    a = 14
    b = 5

    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} = {a // b}")
    print(f"{a} % {b} = {a % b}")
    print(f"{a} ** {b} = {a ** b}")


if __name__ == "__main__":
    main()
