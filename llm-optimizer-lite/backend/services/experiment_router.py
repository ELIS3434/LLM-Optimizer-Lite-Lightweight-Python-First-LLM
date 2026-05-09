import random


def choose_variant(split_percent: int) -> str:
    return "A" if random.randint(1, 100) <= split_percent else "B"
