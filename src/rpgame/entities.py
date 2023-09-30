from abc import ABC


class Entity(ABC):
    def __init__(self, left: float, top: float) -> None:
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
    def __init__(self, left: float, top: float):
        super().__init__(left, top)
        self.inventory = []
    
    def move(self, left: float = 0, top: float = 0) -> None:
        self.left += left
        self.top += top 
        
    def pickup(self, item: Entity):
        if not self.is_in_same_location_as(item):
            raise RuntimeError("Cannot pickup item, it's too far away")
        
        self.inventory.append(item)
    