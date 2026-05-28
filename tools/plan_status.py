"""Show which folders belong to each study plan."""


PLANS = {
    "30-day": [
        "foundations",
        "core_python",
        "modules",
        "engineering",
        "projects",
    ],
    "60-day": [
        "foundations",
        "core_python",
        "modules",
        "pfpython",
        "packaging",
        "standard_library",
        "engineering",
        "tests",
        "advanced",
        "interview",
        "projects",
    ],
    "90-day": [
        "foundations",
        "core_python",
        "modules",
        "pfpython",
        "standard_library",
        "engineering",
        "packaging",
        "tests",
        "advanced",
        "interview",
        "projects",
    ],
}


def main() -> None:
    print("PFPython Study Plan Status")
    print("==========================")
    for plan_name, stages in PLANS.items():
        print(f"\n{plan_name}")
        for stage in stages:
            print(f"- {stage}")


if __name__ == "__main__":
    main()
