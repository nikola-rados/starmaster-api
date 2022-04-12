from fastapi import APIRouter
from app.models.ability_score import AbilityScore
from app.models.character import Character, InMemoryCharacterRepository, NewCharacter
from typing import List
import json

from app.models.constant import ABILITY_CATEGORIES


def characters_from_json(ability_categories: List[str]) -> InMemoryCharacterRepository:
    characters = InMemoryCharacterRepository()
    with open("data/characters.json") as stream:
        for character in json.load(stream):
            ability_scores = [
                AbilityScore(name, score)
                for name, score in zip(ability_categories, character["ability_scores"])
            ]
            characters.create(
                NewCharacter(
                    name=character["name"],
                    ability_scores=ability_scores,
                )
            )

    return characters


router = APIRouter()
characters = characters_from_json(ABILITY_CATEGORIES)


@router.get("/characters")
def get_characters() -> InMemoryCharacterRepository:
    return characters.get_all()


@router.get("/character/{id}")
def get_character_by_id(id: int) -> Character:
    return characters.get(id)
