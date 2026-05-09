def evaluate_output(reference: str, candidate: str) -> float:
    if not reference:
        return 0.0
    return 1.0 if reference.strip().lower() == candidate.strip().lower() else 0.0
