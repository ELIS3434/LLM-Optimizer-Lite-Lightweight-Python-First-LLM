from backend.core.config import settings
from backend.schemas.completion import CompletionRequest
from backend.services.providers.anthropic_provider import AnthropicProvider
from backend.services.providers.base import ProviderAdapter
from backend.services.providers.groq_provider import GroqProvider
from backend.services.providers.ollama_provider import OllamaProvider
from backend.services.providers.openai_provider import OpenAIProvider

PROVIDERS: dict[str, type[ProviderAdapter]] = {
    "openai": OpenAIProvider,
    "anthropic": AnthropicProvider,
    "groq": GroqProvider,
    "ollama": OllamaProvider,
}


def get_provider(name: str) -> ProviderAdapter:
    provider_cls = PROVIDERS.get(name)
    if not provider_cls:
        raise ValueError(f"Unknown provider: {name}")
    return provider_cls()


async def dispatch_completion(payload: CompletionRequest) -> tuple[str, str]:
    provider_name = payload.provider or settings.default_provider
    messages = [m.model_dump() for m in payload.messages]

    try:
        provider = get_provider(provider_name)
        content = await provider.complete(payload.model, messages)
        return content, provider_name
    except Exception:
        fallback = get_provider(settings.fallback_provider)
        fallback_content = await fallback.complete(settings.fallback_model, messages)
        return fallback_content, settings.fallback_provider
