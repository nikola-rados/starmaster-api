from app.models.ability_scores import AbilityScores


class Character:
    def __init__(self, id: int, name: str, ability_scores: AbilityScores):
        self.id = id
        self.name = name
        self.ability_scores = ability_scores
