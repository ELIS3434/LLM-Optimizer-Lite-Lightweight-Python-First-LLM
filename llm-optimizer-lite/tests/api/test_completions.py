from fastapi.testclient import TestClient

from backend.main import app


def test_completion_happy_path() -> None:
    client = TestClient(app)
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "Hello"}],
    }
    response = client.post("/v1/chat/completions", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["model"] == "gpt-4o-mini"
    assert "trace_id" in body
    assert "provider" in body


def test_logs_endpoint_after_completion() -> None:
    client = TestClient(app)
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "Create log"}],
    }
    client.post("/v1/chat/completions", json=payload)
    logs = client.get("/logs")
    assert logs.status_code == 200
    assert isinstance(logs.json(), list)
