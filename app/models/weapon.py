from enum import Enum
from app.models.damage_type import DamageType
from app.models.die import Die


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


class Weapon:
    def __init__(self, id: int, name: str, die: Die, damage_type: DamageType):
        self.id = id
        self.name = name
        self.die = die
        self.damage_type = damage_type

    @property
    def damage_category(self) -> DamageCategory:
        if self.damage_type in KINETIC_DAMAGE_TYPES:
            return DamageCategory.KINETIC

        elif self.damage_type in ENERGY_DAMAGE_TYPES:
            return DamageCategory.ENERGY

        else:
            raise Exception("Unknown damage type")
