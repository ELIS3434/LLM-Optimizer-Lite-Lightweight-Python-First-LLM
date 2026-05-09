import os

import httpx

BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL", "http://localhost:8000")


def get_json(path: str) -> dict | list:
    with httpx.Client(timeout=10) as client:
        response = client.get(f"{BACKEND_BASE_URL}{path}")
        response.raise_for_status()
        return response.json()
