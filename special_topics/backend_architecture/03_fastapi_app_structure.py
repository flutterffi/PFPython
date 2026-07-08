"""Show a FastAPI-style app structure with a safe fallback when FastAPI is missing."""

from dataclasses import dataclass


try:
    from fastapi import FastAPI
except ImportError:  # pragma: no cover - optional dependency path
    FastAPI = None


@dataclass
class AppSettings:
    app_name: str
    debug: bool


class HealthService:
    def health_payload(self) -> dict[str, str]:
        return {"status": "ok", "service": "pfpython-backend-topic"}


def create_app() -> object:
    settings = AppSettings(app_name="PFPython Backend Topic", debug=True)
    service = HealthService()

    if FastAPI is None:
        return {
            "framework": "FastAPI not installed",
            "next_step": "pip install fastapi uvicorn",
            "layers": {
                "settings": settings.app_name,
                "service": service.health_payload(),
                "router": "would call service and return JSON",
            },
        }

    app = FastAPI(title=settings.app_name, debug=settings.debug)

    @app.get("/health")
    def health() -> dict[str, str]:
        return service.health_payload()

    return app


def main() -> None:
    app = create_app()

    print("FastAPI app structure example")
    print("=" * 29)
    if FastAPI is None:
        print(app)
        print("\nInstall command:")
        print("pip install fastapi uvicorn")
        print("Then move this example into a real module name such as app_main.py")
        print("Example: uvicorn app_main:app --reload")
    else:
        print("FastAPI is available.")
        print("Routes:")
        for route in app.routes:
            path = getattr(route, "path", "<unknown>")
            methods = getattr(route, "methods", set())
            print(f"- {path} {sorted(methods)}")


app = create_app()


if __name__ == "__main__":
    main()
