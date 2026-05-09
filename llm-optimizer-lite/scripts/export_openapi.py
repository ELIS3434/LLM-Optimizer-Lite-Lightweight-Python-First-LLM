import json

from backend.main import app


def main() -> None:
    with open("openapi.json", "w", encoding="utf-8") as f:
        json.dump(app.openapi(), f, indent=2)


if __name__ == "__main__":
    main()
