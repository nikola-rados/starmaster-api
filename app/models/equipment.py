from typing import Any, List


class Equipment:
    def __init__(self, items: List[Any]):
        self.items = items

    @property
    def bulk(self) -> int:
        return sum([item.bulk for item in self.items])
