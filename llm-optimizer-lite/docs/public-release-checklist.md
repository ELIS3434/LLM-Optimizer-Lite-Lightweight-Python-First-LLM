# Public Release Checklist (Free OSS)

## Repository readiness
- [x] README with clear value proposition and quickstart
- [x] MIT license present
- [x] Contributing guide present
- [x] CI workflow present
- [x] Security policy present
- [x] Public docs in English

## Safety checks
- [x] `.env.example` contains placeholders only
- [x] No hardcoded API secrets
- [x] Private business assets excluded from public release (`private/` in `.gitignore`)

## Before publishing
- [ ] Run tests locally: `pytest -q`
- [ ] Run lint locally: `ruff check backend dashboard tests`
- [ ] Verify app boots: backend + dashboard

## GitHub publish steps
1. Create empty public repository on GitHub.
2. Push local repository to `main`.
3. Add description and topics from README.
4. Enable Issues and Discussions (optional).
5. Create first release tag `v0.1.0`.
