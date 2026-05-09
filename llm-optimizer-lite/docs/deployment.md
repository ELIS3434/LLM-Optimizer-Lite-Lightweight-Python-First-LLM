# Deployment

## Docker Compose
Run both backend and dashboard:

```bash
docker-compose up --build
```

## Railway
Use `railway.json` with `Dockerfile.backend`.
Set `DATABASE_URL` and provider keys.

## Fly.io
Use `fly.toml` and run:

```bash
fly deploy
```

## Required environment variables
- `DATABASE_URL`
- `DEFAULT_PROVIDER`
- `DEFAULT_MODEL`
- Provider API keys (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, etc.)

## Production caveats
Use PostgreSQL for production, tighten API-key policy, and add persistent log retention.
