from fastapi import APIRouter
from app.models.ability_scores import AbilityScores
from app.models.character import Character
from typing import List
import json

router = APIRouter()


def characters_from_json():
    with open("data/characters.json") as stream:
        characters = [
            Character(
                id=character["id"],
                name=character["name"],
                ability_scores=AbilityScores(*character["ability_scores"]),
            )
            for character in json.load(stream)
        ]
    return characters


@router.get("/characters")
def get_characters():
    return characters_from_json()


@router.get("/character/{id}")
def get_character_by_id(id: int):
    return next(character for character in characters_from_json() if character.id == id)
