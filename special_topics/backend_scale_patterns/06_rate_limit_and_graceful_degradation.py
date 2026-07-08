"""Practice rate limiting and graceful degradation behavior."""

from dataclasses import dataclass


@dataclass
class RateLimitWindow:
    allowed: int
    used: int = 0


def handle_request(window: RateLimitWindow) -> dict[str, object]:
    if window.used >= window.allowed:
        return {
            "status": "degraded",
            "response_mode": "fallback",
            "message": "Serve cached summary instead of full live response.",
        }

    window.used += 1
    return {
        "status": "ok",
        "response_mode": "live",
        "used": window.used,
    }


def main() -> None:
    window = RateLimitWindow(allowed=2)
    first = handle_request(window)
    second = handle_request(window)
    third = handle_request(window)

    print("Rate limit flow")
    print("=" * 15)
    print(first)
    print(second)
    print(third)
    print("\nHigh-level questions:")
    print("- when should a service reject vs degrade")
    print("- what fallback is safe enough to serve")
    print("- should limits be per user, per token, or per IP")


if __name__ == "__main__":
    main()
