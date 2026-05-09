def resolve_prompt(prompt_name: str | None, fallback: str) -> str:
    return prompt_name or fallback
