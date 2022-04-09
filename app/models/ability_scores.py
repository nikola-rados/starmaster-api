from app.models.ability_score import AbilityScore


class AbilityScores:
    def __init__(
        self,
        strength: AbilityScore,
        dexterity: AbilityScore,
        constitution: AbilityScore,
        intelligence: AbilityScore,
        wisdom: AbilityScore,
        charisma: AbilityScore,
    ):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
