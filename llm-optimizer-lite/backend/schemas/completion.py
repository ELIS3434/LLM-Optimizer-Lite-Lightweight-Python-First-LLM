from pydantic import BaseModel, Field


class Message(BaseModel):
    role: str
    content: str


class CompletionRequest(BaseModel):
    model: str
    messages: list[Message]
    provider: str | None = Field(default=None, description="Optional provider override")


class CompletionResponse(BaseModel):
    model: str
    content: str
    provider: str
    estimated_cost_usd: float
    trace_id: str
    latency_ms: int
