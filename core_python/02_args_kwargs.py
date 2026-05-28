"""Core lesson 02: flexible function arguments."""


def build_label(title: str, *tags: str, uppercase: bool = False, **metadata: str) -> str:
    label = title.upper() if uppercase else title
    tag_text = ", ".join(tags) if tags else "no tags"
    metadata_text = ", ".join(f"{key}={value}" for key, value in metadata.items()) or "no metadata"
    return f"{label} | tags: {tag_text} | metadata: {metadata_text}"


def main() -> None:
    label = build_label(
        "practice session",
        "python",
        "functions",
        uppercase=True,
        level="intermediate",
        status="active",
    )
    print(label)


if __name__ == "__main__":
    main()
