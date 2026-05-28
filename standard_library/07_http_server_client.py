"""Standard library lesson 07: model a tiny HTTP request and response flow."""

from http import HTTPStatus
from urllib.parse import parse_qs, urlencode, urlsplit
import json


def build_url(base_url: str, params: dict[str, str]) -> str:
    return f"{base_url}?{urlencode(params)}"


def simulate_server(url: str) -> tuple[int, str]:
    parsed = urlsplit(url)
    query = parse_qs(parsed.query)
    topic = query.get("topic", ["unknown"])[0]
    payload = json.dumps(
        {
            "path": parsed.path,
            "topic": topic,
            "message": "HTTP concepts without external networking",
        }
    )
    return HTTPStatus.OK.value, payload


def main() -> None:
    url = build_url("http://localhost/practice", {"topic": "http-basics", "level": "core"})
    status_code, response_body = simulate_server(url)

    print(f"{url = }")
    print(f"{status_code = }")
    print(json.loads(response_body))


if __name__ == "__main__":
    main()
