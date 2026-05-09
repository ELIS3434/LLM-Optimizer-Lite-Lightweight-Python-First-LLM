from datetime import UTC, datetime

LOGS: list[dict[str, int | float | str]] = []


def build_log_record(
    model: str,
    provider: str,
    latency_ms: int,
    estimated_cost_usd: float,
    status: str,
    trace_id: str,
) -> dict[str, int | float | str]:
    return {
        "trace_id": trace_id,
        "provider": provider,
        "model": model,
        "latency_ms": latency_ms,
        "estimated_cost_usd": estimated_cost_usd,
        "status": status,
        "created_at": datetime.now(UTC).isoformat(),
    }


def append_log(entry: dict[str, int | float | str]) -> None:
    LOGS.append(entry)


def list_logs(limit: int = 100) -> list[dict[str, int | float | str]]:
    return LOGS[-limit:]
