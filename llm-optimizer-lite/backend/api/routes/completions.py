import time
import uuid

from fastapi import APIRouter, Depends, Header, HTTPException

from backend.core.config import settings
from backend.core.security import validate_api_key
from backend.schemas.completion import CompletionRequest, CompletionResponse
from backend.services.cost_estimator import estimate_cost
from backend.services.provider_registry import dispatch_completion
from backend.services.request_tracker import append_log, build_log_record

router = APIRouter(prefix="/v1", tags=["completions"])


def _auth(x_api_key: str | None = Header(default=None)) -> None:
    ok = validate_api_key(settings.api_key_enabled, settings.internal_api_key, x_api_key)
    if not ok:
        raise HTTPException(status_code=401, detail="Invalid API key")


@router.post("/chat/completions", response_model=CompletionResponse)
async def create_completion(payload: CompletionRequest, _: None = Depends(_auth)) -> CompletionResponse:
    started = time.perf_counter()
    text, provider_used = await dispatch_completion(payload)
    latency_ms = int((time.perf_counter() - started) * 1000)
    cost = estimate_cost(payload.model, payload.messages)
    trace_id = str(uuid.uuid4())

    append_log(
        build_log_record(
            model=payload.model,
            provider=provider_used,
            latency_ms=latency_ms,
            estimated_cost_usd=cost,
            status="ok",
            trace_id=trace_id,
        )
    )

    return CompletionResponse(
        model=payload.model,
        content=text,
        provider=provider_used,
        estimated_cost_usd=cost,
        trace_id=trace_id,
        latency_ms=latency_ms,
    )
