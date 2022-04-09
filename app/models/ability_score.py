class AbilityScore:
    def __init__(self, name: str, score: int, is_key: bool = False):
        self.name = name
        self.score = score
        self.is_key = is_key

    @property
    def modifier(self):
        return int(self.score / 2) - 5
