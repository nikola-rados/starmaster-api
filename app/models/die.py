from enum import Enum
from random import randint


class DieOptions(Enum):
    dPercent = 100
    d20 = 20
    d12 = 12
    d10 = 10
    d8 = 8
    d6 = 6
    d4 = 4


class Die:
    def __init__(self, die: DieOptions):
        self.die = die

    def roll(self) -> int:
        return randint(1, self.die.value)
