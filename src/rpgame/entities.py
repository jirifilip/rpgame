from abc import ABC
from dataclasses import dataclass
from typing import List


@dataclass
class Entity(ABC):
    left: int
    top: int

    def is_in_same_location_as(self, other_entity: "Entity") -> bool:
        location = self.left, self.top
        other_location = other_entity.left, other_entity.top

        return location == other_location


@dataclass
class Wall(Entity):
    pass


@dataclass
class Gold(Entity):
    pass


@dataclass
class Player(Entity):
    def __post_init__(self):
        self.inventory: List[Entity] = []

    def move(self, left: int = 0, top: int = 0) -> None:
        self.left += left
        self.top += top

    def pickup(self, item: Entity):
        if not self.is_in_same_location_as(item):
            raise RuntimeError("Cannot pickup item, it's too far away")

        self.inventory.append(item)
