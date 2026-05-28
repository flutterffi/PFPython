"""Interview lesson 02: check palindromes with normalization."""


def is_palindrome(text: str) -> bool:
    normalized = "".join(character.lower() for character in text if character.isalnum())
    return normalized == normalized[::-1]


def main() -> None:
    samples = [
        "level",
        "A man, a plan, a canal: Panama",
        "python",
    ]
    for sample in samples:
        print(f"{sample!r}: {is_palindrome(sample)}")


if __name__ == "__main__":
    main()
