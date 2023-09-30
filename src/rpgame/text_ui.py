from typing import List, Tuple

from rpgame.entities import Emptiness, Player, Wall
from rpgame.utils import create_2d_list, stringify_2d_list


class TextUI:
    """renders game as text"""

    _CHARACTER_TO_ENTITY_FACTORY = {
        "@": Player,
        "|": Wall,
        "_": Wall,
    }
    _ENTITY_TYPE_TO_CHARACTER = {
        Player: "@",
        Wall: "|",
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
        width, height = self.room_dimensions
        characters = create_2d_list(width, height, fill=" ")
        
        for entity in self.entities:
            character = self._ENTITY_TYPE_TO_CHARACTER[type(entity)]
            characters[entity.top][entity.left] = character         
            
        return stringify_2d_list(
            characters,
            row_separator="\n",
            column_separator=""
        )

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

    
