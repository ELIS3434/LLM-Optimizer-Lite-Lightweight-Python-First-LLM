from fastapi.testclient import TestClient

from backend.main import app


def get_client() -> TestClient:
    return TestClient(app)
