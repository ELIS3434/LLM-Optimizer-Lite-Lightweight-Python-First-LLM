# Workflow

## Local development
1. Copy `.env.example` to `.env`.
2. Install dependencies.
3. Start backend and dashboard.
4. Create prompts and experiments.
5. Review analytics and logs.

## Prompt lifecycle
Create template -> create version -> assign active version -> observe production behavior.

## Experiment lifecycle
Create experiment -> define variants and split -> route traffic -> review outcomes.

## Release workflow
- Run lint and tests.
- Update docs for API or architecture changes.
- Build and deploy with Docker, Railway, or Fly.io.

## Cursor contribution workflow
Cursor agents should follow `.cursor/rules/project.mdc`, keep public outputs in English, and update tests/docs with behavior changes.
