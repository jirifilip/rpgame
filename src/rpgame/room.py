from rpgame.entities import Entity, Gold, Player, Wall


from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True, repr=True)
class Room:
    dimensions: Tuple[int, int]
    entities: List[Entity]

    _CHARACTER_TO_ENTITY_FACTORY = {
        "@": Player,
        "|": Wall,
        "o": Gold
    }

    @classmethod
    def from_text_map(cls, text_map: str):
        text_map_lines = text_map.strip().split("\n")

        room_dimensions = cls._extract_room_dimensions(text_map_lines)

        entities = cls._convert_text_map_to_entities(text_map_lines)
        return cls(dimensions=room_dimensions, entities=entities)

    @staticmethod
    def _extract_room_dimensions(text_map_lines: List[str]) -> Tuple[int, int]:
        height = len(text_map_lines)
        width = len(text_map_lines[0])

        return width, height

    @staticmethod
    def _convert_text_map_to_entities(text_map_lines: List[str]) -> List[Entity]:
        factory_map = Room._CHARACTER_TO_ENTITY_FACTORY

        return [
            factory_map[character](left_idx, top_idx)
            for top_idx, row in enumerate(text_map_lines)
            for left_idx, character in enumerate(row)
            if character in factory_map
        ]
