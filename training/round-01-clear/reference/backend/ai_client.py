import json
import os
import urllib.error
import urllib.request

from dotenv import load_dotenv

load_dotenv()


class AIClientError(RuntimeError):
    pass


def generate_reply(messages: list[dict[str, str]]) -> str:
    url = os.getenv("AI_API_URL")
    api_key = os.getenv("AI_API_KEY")
    model = os.getenv("AI_MODEL")

    if not url or not api_key or not model or "example.invalid" in url:
        raise AIClientError("AI API environment variables are not configured")

    payload = json.dumps({"model": model, "messages": messages}).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise AIClientError(f"AI API request failed: {type(exc).__name__}") from exc

    try:
        content = body["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise AIClientError("AI API response shape is unsupported") from exc

    if not isinstance(content, str) or not content.strip():
        raise AIClientError("AI API returned an empty response")
    return content.strip()
