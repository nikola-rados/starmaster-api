from random import randint
from app.models.die import Die


class AbilityScoreGenerator:
    """Typically the die should be a d6, but we are leaving it as an open option for the sake of better code."""
    def __init__(self, die: Die):
        self.die = die

    def roll_score(self) -> int:
        rolls = [randint(1, self.die) for i in range(4)]
        rolls.remove(min(rolls))
        return sum(rolls)
