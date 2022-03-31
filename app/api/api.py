import json

from app.db.models import Character


def read_characters():
    with open("data/characters.json") as stream:
        characters = [
            Character(id=character.id, name=character.name, health=character.health)
            for character in json.load(stream)
        ]

    return characters


def read_character_by_id(id: int) -> Character:
    return next(character for character in read_characters() if character.id == id)

def rest_character(id: int, character: Character):
    result = {"id": id, **character.dict()}
    result.update({"health": 100})
    return result