from rpgame.entities import Entity, Gold, Player


from typing import List


class Game:
    def __init__(self, player: Player, entities: List[Entity]):
        self.player = player
        self.entities = entities

    def move_player(self, left: float = 0, top: float = 0) -> None:
        self.player.move(left, top)

        for entity in self.entities:
            if entity == self.player:
                continue
            
            if self.player.is_in_same_location_as(entity) and type(entity) == Gold:
                self.player.pickup(entity)
                self.entities.remove(entity)

    @property
    def player_inventory(self):
        return self.player.inventory