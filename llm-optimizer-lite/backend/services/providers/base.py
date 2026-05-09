from abc import ABC, abstractmethod


class ProviderAdapter(ABC):
    @abstractmethod
    async def complete(self, model: str, messages: list[dict[str, str]]) -> str:
        raise NotImplementedError
