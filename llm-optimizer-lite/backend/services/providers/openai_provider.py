from backend.services.providers.base import ProviderAdapter


class OpenAIProvider(ProviderAdapter):
    async def complete(self, model: str, messages: list[dict[str, str]]) -> str:
        prompt = messages[-1]["content"] if messages else ""
        return f"[openai:{model}] {prompt}".strip()
