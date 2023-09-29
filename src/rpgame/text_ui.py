from rpgame.entities import Player, Wall


class TextUI:
    """renders game as text"""

    _CHARACTER_TO_ENTITY_FACTORY = {
        "@": Player,
        "|": Wall,
        "_": Wall
    }

    def __init__(self, initial_state: str, entities = None):
        self.state = initial_state
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
    def _convert_text_map_to_entities(text_map: str):
        factory_map = TextUI._CHARACTER_TO_ENTITY_FACTORY
        text_map_rows = text_map.strip().split("\n")        

        return [
            factory_map[character](left_idx, top_idx)
            for top_idx, row in enumerate(text_map_rows)
            for left_idx, character in enumerate(row)
            if character in factory_map
        ]


    @classmethod
    def from_map(cls, text_map: str):
        entities = cls._convert_text_map_to_entities(text_map)
        return TextUI(initial_state="", entities=entities)