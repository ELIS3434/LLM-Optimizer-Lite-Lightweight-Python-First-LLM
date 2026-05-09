from pydantic import BaseModel


class SummaryOut(BaseModel):
    total_requests: int
    total_estimated_cost_usd: float
    p95_latency_ms: int


class TimeseriesPoint(BaseModel):
    ts: str
    requests: int
    estimated_cost_usd: float
