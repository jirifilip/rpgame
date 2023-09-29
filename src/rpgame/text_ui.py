from rpgame.entities import Player, Wall


class TextUI:
    """renders game as text"""

    _CHARACTER_TO_ENTITY_CLASS = {
        "@": Player,
        "|": Wall,
        "_": Wall
    }

    def __init__(self, initial_state: str, entities = None):
        self.state = initial_state
        self.entities = entities

    def render(self) -> str:
        #return self.state
        return (
"""
|-----|
|     |
| @   |
|-----|
"""
        )

    @classmethod
    def from_map(cls, map: str):
        entity_classes_or_none = [
            cls._CHARACTER_TO_ENTITY_CLASS.get(character)
            for character in map
        ]
        entities = [
            entity_class(0, 0) for entity_class in entity_classes_or_none
            if entity_class
        ]
        return TextUI(initial_state="", entities=entities)