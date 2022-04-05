from fastapi import APIRouter
from app.models.weapon import Weapon, Bulk
from app.models.die import Die, DieOptions
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
                dice=[Die(DieOptions[die]) for die in weapon["dice"]],
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


@router.get("/weapon/{id}/roll")
def roll_weapon_damage_by_id(id: float):
    weapon = weapon_by_id(id)
    return {"damage": weapon.roll_damage()}
