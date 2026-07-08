"""Practice idempotency keys and safe retry behavior."""

from dataclasses import dataclass


@dataclass
class ChargeRequest:
    idempotency_key: str
    user_id: str
    amount: int


class PaymentProcessor:
    def __init__(self) -> None:
        self.processed: dict[str, dict[str, object]] = {}

    def charge(self, request: ChargeRequest) -> dict[str, object]:
        cached = self.processed.get(request.idempotency_key)
        if cached is not None:
            return {
                "mode": "replay",
                "response": cached,
            }

        response = {
            "status": "accepted",
            "user_id": request.user_id,
            "amount": request.amount,
        }
        self.processed[request.idempotency_key] = response
        return {
            "mode": "new",
            "response": response,
        }


def main() -> None:
    processor = PaymentProcessor()
    request = ChargeRequest(idempotency_key="pay-100", user_id="learner-7", amount=99)

    first = processor.charge(request)
    second = processor.charge(request)

    print("Idempotency flow")
    print("=" * 16)
    print(first)
    print(second)
    print("\nHigh-level questions:")
    print("- where should idempotency records be stored")
    print("- how long should keys live")
    print("- what if same key arrives with different payload data")


if __name__ == "__main__":
    main()
