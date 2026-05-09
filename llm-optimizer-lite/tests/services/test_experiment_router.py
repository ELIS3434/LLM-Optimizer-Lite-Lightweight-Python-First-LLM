from backend.services.experiment_router import choose_variant


def test_experiment_router_returns_known_variant() -> None:
    variant = choose_variant(50)
    assert variant in {"A", "B"}
