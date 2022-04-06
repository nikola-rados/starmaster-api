from enum import Enum
from app.models.damage_type import DamageType
from app.models.die import Die
from typing import List


KINETIC_DAMAGE_TYPES = [
    DamageType.BLUDGEONING,
    DamageType.PIERCING,
    DamageType.SLASHING,
]

ENERGY_DAMAGE_TYPES = [
    DamageType.ACID,
    DamageType.COLD,
    DamageType.ELECTRICITY,
    DamageType.FIRE,
    DamageType.SONIC,
]


class DamageCategory(Enum):
    KINETIC = "kinetic"
    ENERGY = "energy"


class Bulk(Enum):
    NEGLIGABLE = 0.0
    LIGHT = 0.1
    NORMAL = 1.0
    HEAVY = 2.0
    SUPREME = 3.0


class Weapon:
    def __init__(
        self, id: int, name: str, dice: List[Die], damage_type: DamageType, bulk: Bulk
    ):
        self.id = id
        self.name = name
        self.dice = dice
        self.damage_type = damage_type
        self.bulk = bulk

    @property
    def damage_category(self) -> DamageCategory:
        if self.damage_type in KINETIC_DAMAGE_TYPES:
            return DamageCategory.KINETIC

        elif self.damage_type in ENERGY_DAMAGE_TYPES:
            return DamageCategory.ENERGY

        else:
            raise Exception("Unknown damage type")
