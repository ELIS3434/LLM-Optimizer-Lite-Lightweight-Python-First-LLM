from backend.services.providers.base import ProviderAdapter


class GroqProvider(ProviderAdapter):
    async def complete(self, model: str, messages: list[dict[str, str]]) -> str:
        prompt = messages[-1]["content"] if messages else ""
        return f"[groq:{model}] {prompt}".strip()
