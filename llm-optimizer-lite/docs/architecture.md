# Architecture

LLM Optimizer Lite is a modular Python monolith:
- FastAPI backend (`backend/`)
- Streamlit dashboard (`dashboard/`)
- Shared SQL database

## Request lifecycle
1. Client calls `/v1/chat/completions`.
2. Prompt engine resolves prompt/version.
3. Experiment router selects variant if configured.
4. Provider adapter sends request upstream.
5. Response is normalized and tracked.
6. Usage, latency, and estimated cost are stored.

## Provider abstraction
Each provider implements a shared adapter interface in `backend/services/providers`.

## Data model overview
Core entities include prompt templates/versions, experiments, request logs, and evaluation runs.

## Why modular monolith
This keeps setup and operations simple while preserving clear extension boundaries.
