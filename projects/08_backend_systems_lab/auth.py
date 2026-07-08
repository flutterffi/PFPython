"""Authorization flow for the backend systems lab."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from models import RequestContext


def ensure_scope(context: RequestContext, required_scope: str) -> dict[str, object]:
    allowed = required_scope in context.scopes
    return {
        "request_id": context.request_id,
        "authorized": allowed,
        "required_scope": required_scope,
    }


def main() -> None:
    context = RequestContext(
        request_id="req-auth",
        subject="learner-1",
        topic="observability",
        scopes={"read:topics"},
        idempotency_key="idem-auth",
    )
    print("Auth lab demo")
    print("=" * 13)
    print(ensure_scope(context, "read:topics"))


if __name__ == "__main__":
    main()
