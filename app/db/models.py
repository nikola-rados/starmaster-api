from lib2to3.pytree import Base
from pydantic import BaseModel


class Character(BaseModel):
    id: int
    name: str
    health: int
