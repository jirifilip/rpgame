from abc import ABC
from typing import List


class Entity(ABC):
    def __init__(self, left: int, top: int) -> None:
        super().__init__()
        self.left = left
        self.top = top

    def is_in_same_location_as(self, other_entity: "Entity") -> bool:
        location = self.left, self.top
        other_location = other_entity.left, other_entity.top

        return location == other_location


class Wall(Entity):
    pass


class Gold(Entity):
    pass


class Player(Entity):
    def __init__(self, left: int, top: int):
        super().__init__(left, top)
        self.inventory: List[Entity] = []

    def move(self, left: int = 0, top: int = 0) -> None:
        self.left += left
        self.top += top

    def pickup(self, item: Entity):
        if not self.is_in_same_location_as(item):
            raise RuntimeError("Cannot pickup item, it's too far away")

        self.inventory.append(item)
