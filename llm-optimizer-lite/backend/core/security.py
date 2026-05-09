def validate_api_key(enabled: bool, expected: str, actual: str | None) -> bool:
    if not enabled:
        return True
    return bool(actual and actual == expected)
