# Contributing

Thanks for contributing to LLM Optimizer Lite.

## Local workflow
1. Create a feature branch.
2. Install dependencies (`pip install -r requirements.txt`).
3. Run tests (`pytest -q`).
4. Run lint checks (`ruff check backend dashboard tests`).
5. Update docs when API or architecture changes.

## Engineering standards
- Python 3.11+
- Type hints required
- Keep business logic in `backend/services`
- Keep routes thin and schemas explicit
- Add or update tests with logic changes

## Pull requests
Use the PR template and include:
- What changed
- Why it changed
- Test plan
