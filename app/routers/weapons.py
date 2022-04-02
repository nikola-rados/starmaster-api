from fastapi import APIRouter
from app.models.weapon import Weapon
from typing import List
import json

router = APIRouter()


def weapons_from_json():
    with open("data/weapons.json") as stream:
        weapons = [
            Weapon(
                id=weapon["id"],
                name=weapon["name"],
                die=weapon["die"],
                damage_type=weapon["damage_type"],
            )
            for weapon in json.load(stream)
        ]
    return weapons


@router.get("/weapons")
def get_weapons():
    return weapons_from_json()


@router.get("/weapon/{id}")
def get_weapon_by_id(id: int):
    return next(weapon for weapon in weapons_from_json() if weapon.id == id)
