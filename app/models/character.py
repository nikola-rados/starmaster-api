from unicodedata import name
from app.models.ability_score import AbilityScore
from app.models.equipment import Equipment
import itertools
from typing import List


class Character:
    def __init__(
        self,
        id: int,
        name: str,
        ability_scores: List[AbilityScore],  # , equipment: Equipment
    ):
        self.id = id
        self.name = name
        self.ability_scores = ability_scores
        # self.equipment = equipment


class NewCharacter:
    def __init__(
        self, name: str, ability_scores: List[AbilityScore]  # , equipment: Equipment
    ):
        self.name = name
        self.name = name
        self.ability_scores = ability_scores
        # self.equipment = equipment


# Character "interface"
class CharacterRepository:
    def get(self, character_id: int) -> Character:
        pass

    def get_all(self) -> List[Character]:
        pass

    def create(self, character: NewCharacter) -> Character:
        pass


class InMemoryCharacterRepository(CharacterRepository):
    id_iter = itertools.count()

    def __init__(self):
        self.characters = {}

    def get(self, character_id: int) -> Character:
        return self.characters[character_id]

    def get_all(self):
        return self.characters

    def create(self, new_character: NewCharacter) -> Character:
        character = self._build_character(new_character)
        self.characters[character.id] = character
        return character

    def _build_character(self, new_character: NewCharacter) -> Character:
        return Character(
            id=next(InMemoryCharacterRepository.id_iter),
            name=new_character.name,
            ability_scores=new_character.ability_scores,
        )
