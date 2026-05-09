from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "LLM Optimizer Lite"
    database_url: str = "sqlite+aiosqlite:///./llm_optimizer.db"
    default_provider: str = "openai"
    default_model: str = "gpt-4o-mini"
    fallback_provider: str = "ollama"
    fallback_model: str = "llama3"
    api_key_enabled: bool = False
    internal_api_key: str = "dev-key"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
