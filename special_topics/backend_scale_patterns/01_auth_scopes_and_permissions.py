"""Practice scope-based authorization flow in a backend service."""

from dataclasses import dataclass


@dataclass
class AccessToken:
    subject: str
    scopes: set[str]


@dataclass
class ProtectedAction:
    name: str
    required_scopes: set[str]


def authorize(token: AccessToken, action: ProtectedAction) -> dict[str, object]:
    missing_scopes = sorted(action.required_scopes - token.scopes)
    return {
        "subject": token.subject,
        "action": action.name,
        "authorized": not missing_scopes,
        "missing_scopes": missing_scopes,
    }


def main() -> None:
    token = AccessToken(subject="learner-42", scopes={"read:topics", "read:logs"})
    action = ProtectedAction(
        name="view_observability_dashboard",
        required_scopes={"read:topics", "read:metrics"},
    )
    result = authorize(token, action)

    print("Authorization flow")
    print("=" * 18)
    print(result)
    print("\nHigh-level questions:")
    print("- should scope checks happen in the router, dependency, or service")
    print("- which failures should be 401 vs 403")
    print("- which audit events should be logged")


if __name__ == "__main__":
    main()
