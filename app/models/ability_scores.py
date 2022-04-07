from app.models.ability_score_generator import AbilityScoreGenerator
from app.models.die import Die


class AbilityScores:
    def __init__(
        self,
        strength: int = None,
        dexterity: int = None,
        constitution: int = None,
        intelligence: int = None,
        wisdom: int = None,
        charisma: int = None,
    ):
        score_generator = AbilityScoreGenerator(Die["d6"])

        self.strength = strength if strength else score_generator.roll_score()
        self.dexterity = dexterity if dexterity else score_generator.roll_score()
        self.constitution = constitution if constitution else score_generator.roll_score()
        self.intelligence = intelligence if intelligence else score_generator.roll_score()
        self.wisdom = wisdom if wisdom else score_generator.roll_score()
        self.charisma = charisma if charisma else score_generator.roll_score()
