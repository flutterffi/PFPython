"""Service orchestration for the backend systems lab."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from auth import ensure_scope
from cache_layer import TopicCache
from idempotency import IdempotencyStore
from jobs import JobQueue
from models import RequestContext, TopicSummary
from observability import build_snapshot


class SystemsLabService:
    def __init__(self) -> None:
        self.cache = TopicCache()
        self.idempotency = IdempotencyStore()
        self.jobs = JobQueue()

    def handle_request(self, context: RequestContext) -> dict[str, object]:
        cached = self.idempotency.get(context.idempotency_key)
        if cached is not None:
            return {"mode": "replay", "response": cached}

        auth_result = ensure_scope(context, "read:topics")
        if not auth_result["authorized"]:
            response = {"status": "forbidden", "request_id": context.request_id}
            self.idempotency.remember(context.idempotency_key, response)
            return {"mode": "new", "response": response}

        cached_summary = self.cache.get(context.topic)
        cache_hit = cached_summary is not None
        summary = cached_summary or TopicSummary(
            topic=context.topic,
            source="repository",
            message=f"Prepared advanced training summary for {context.topic}.",
        )
        if not cache_hit:
            self.cache.set(summary)

        job = self.jobs.schedule(f"refresh:{context.topic}")
        snapshot = build_snapshot(latency_ms=48, cache_hit=cache_hit, job_count=len(self.jobs.scheduled))
        response = {
            "status": "ok",
            "topic": summary.to_dict(),
            "job": {"name": job.name, "state": job.state},
            "observability": snapshot,
        }
        self.idempotency.remember(context.idempotency_key, response)
        return {"mode": "new", "response": response}


def main() -> None:
    service = SystemsLabService()
    context = RequestContext(
        request_id="req-service",
        subject="learner-2",
        topic="observability",
        scopes={"read:topics", "read:metrics"},
        idempotency_key="idem-service",
    )
    print("Service lab demo")
    print("=" * 16)
    print(service.handle_request(context))


if __name__ == "__main__":
    main()
