from fastapi.testclient import TestClient

from backend.main import app


def test_prompt_create_and_list() -> None:
    client = TestClient(app)
    create_response = client.post("/prompts", json={"name": "support_prompt"})
    assert create_response.status_code == 200

    list_response = client.get("/prompts")
    assert list_response.status_code == 200
    assert isinstance(list_response.json(), list)
