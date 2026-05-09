from collections import defaultdict

from fastapi import APIRouter

from backend.schemas.analytics import SummaryOut, TimeseriesPoint
from backend.services.request_tracker import list_logs

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/summary", response_model=SummaryOut)
async def summary() -> SummaryOut:
    logs = list_logs(1000)
    total_requests = len(logs)
    total_cost = sum(float(item.get("estimated_cost_usd", 0.0)) for item in logs)
    latencies = [int(item.get("latency_ms", 0)) for item in logs]
    p95 = sorted(latencies)[int(0.95 * (len(latencies) - 1))] if latencies else 0
    return SummaryOut(total_requests=total_requests, total_estimated_cost_usd=round(total_cost, 6), p95_latency_ms=p95)


@router.get("/timeseries", response_model=list[TimeseriesPoint])
async def timeseries() -> list[TimeseriesPoint]:
    grouped: dict[str, dict[str, float | int]] = defaultdict(lambda: {"requests": 0, "estimated_cost_usd": 0.0})
    for item in list_logs(1000):
        ts = str(item.get("created_at", ""))[:16]
        grouped[ts]["requests"] += 1
        grouped[ts]["estimated_cost_usd"] += float(item.get("estimated_cost_usd", 0.0))

    out: list[TimeseriesPoint] = []
    for ts, values in sorted(grouped.items()):
        out.append(
            TimeseriesPoint(
                ts=ts,
                requests=int(values["requests"]),
                estimated_cost_usd=round(float(values["estimated_cost_usd"]), 6),
            )
        )
    return out
