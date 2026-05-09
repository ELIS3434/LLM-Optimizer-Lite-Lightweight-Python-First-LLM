.PHONY: run-backend run-dashboard test lint format

run-backend:
	uvicorn backend.main:app --reload

run-dashboard:
	streamlit run dashboard/app.py

test:
	pytest -q

lint:
	ruff check backend dashboard tests
	mypy backend

format:
	ruff format backend dashboard tests
