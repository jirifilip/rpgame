from typing import List, Tuple

from rpgame.entities import Player, Wall


class TextUI:
    """renders game as text"""

    _CHARACTER_TO_ENTITY_FACTORY = {
        "@": Player,
        "|": Wall,
        "_": Wall
    }

    def __init__(
            self,
            initial_state: str,
            room_dimensions: Tuple[int, int],
            entities = None,
        ):
        self.state = initial_state
        self.room_dimensions = room_dimensions
        self.entities = entities

    def render(self) -> str:
        entity_type_to_character = {
            Player: "@",
            Wall: "|"
        }
        
        return "".join([
            entity_type_to_character[type(entity)]
            for entity in self.entities
        ])
            
        
    @staticmethod
    def _convert_text_map_to_entities(text_map_matrix: List[List[str]]):
        factory_map = TextUI._CHARACTER_TO_ENTITY_FACTORY

        return [
            factory_map[character](left_idx, top_idx)
            for top_idx, row in enumerate(text_map_matrix)
            for left_idx, character in enumerate(row)
            if character in factory_map
        ]
        
    @staticmethod
    def _extract_room_dimensions(text_map_matrix: List[List[str]]):
        height = len(text_map_matrix)
        width = len(text_map_matrix[0])
        
        return width, height

    @classmethod
    def from_map(cls, text_map: str):
        text_map_matrix = text_map.strip().split("\n")
        
        room_dimensions = cls._extract_room_dimensions(text_map_matrix)
        
        entities = cls._convert_text_map_to_entities(text_map_matrix)
        return TextUI(initial_state="", room_dimensions=room_dimensions, entities=entities)

    
