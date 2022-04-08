from fastapi import APIRouter
from app.models.ability_scores import AbilityScores
from app.models.character import Character, InMemoryCharacterRepository, NewCharacter
from typing import List
import json


def characters_from_json() -> InMemoryCharacterRepository:
    characters = InMemoryCharacterRepository()
    with open("data/characters.json") as stream:
        for character in json.load(stream):
            characters.create(
                NewCharacter(
                    name=character["name"],
                    ability_scores=AbilityScores(*character["ability_scores"]),
                )
            )

    return characters


router = APIRouter()
characters = characters_from_json()


@router.get("/characters")
def get_characters() -> InMemoryCharacterRepository:
    return characters.get_all()


@router.get("/character/{id}")
def get_character_by_id(id: int) -> Character:
    return characters.get(id)
