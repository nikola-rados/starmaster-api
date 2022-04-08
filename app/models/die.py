class Die:
    def __init__(self, sides: int):
        self.sides = sides

    def __repr__(self) -> str:
        return f"d{self.sides}"
