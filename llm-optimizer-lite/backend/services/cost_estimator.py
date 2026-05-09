from backend.core.pricing import MODEL_PRICING
from backend.schemas.completion import Message


def estimate_cost(model: str, messages: list[Message]) -> float:
    pricing = MODEL_PRICING.get(model)
    if not pricing:
        return 0.0
    input_chars = sum(len(m.content) for m in messages)
    input_tokens_est = max(1, input_chars // 4)
    return round(input_tokens_est * pricing["input"], 8)
