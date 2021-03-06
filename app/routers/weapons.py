from fastapi import APIRouter
from app.models.weapon import Weapon, Bulk
from app.models.die import Die
from app.models.damage_type import DamageType
from typing import List
import json

router = APIRouter()


def weapons_from_json() -> List[Weapon]:
    with open("data/weapons.json") as stream:
        weapons = [
            Weapon(
                id=weapon["id"],
                name=weapon["name"],
                dice=[Die(sides) for sides in weapon["dice"]],
                damage_type=DamageType(weapon["damage_type"]),
                bulk=Bulk[weapon["bulk"]],
            )
            for weapon in json.load(stream)
        ]
    return weapons


def weapon_by_id(id: int):
    return next(weapon for weapon in weapons_from_json() if weapon.id == id)


@router.get("/weapons")
def get_weapons():
    return weapons_from_json()


@router.get("/weapon/{id}")
def get_weapon_by_id(id: int):
    return weapon_by_id(id)
