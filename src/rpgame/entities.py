from abc import ABC


class Entity(ABC):
    pass


class Wall(Entity):
    def __init__(self, left: float, top: float):
        self.left = left
        self.top = top


class Player(Entity):
    def __init__(self, left: float, top: float):
        self.left = left
        self.top = top
    
    def move(self, left: float = 0, top: float = 0) -> None:
        self.left += left
        self.top += top 
