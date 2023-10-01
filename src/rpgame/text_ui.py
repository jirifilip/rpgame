from typing import Dict
from typing import Type

from rpgame.entities import Entity
from rpgame.entities import Gold
from rpgame.entities import Player
from rpgame.entities import Wall
from rpgame.room import Room
from rpgame.utils import create_2d_list
from rpgame.utils import stringify_2d_list


class TextUI:
    """renders game as text"""

    _ENTITY_TYPE_TO_CHARACTER: Dict[Type[Entity], str] = {
        Player: "@",
        Wall: "|",
        Gold: "o"
    }

    @staticmethod
    def render(room: Room) -> str:
        width, height = room.dimensions
        render_matrix = create_2d_list(width, height, fill=" ")

        for entity in room.entities:
            character = TextUI._ENTITY_TYPE_TO_CHARACTER[type(entity)]
            render_matrix[entity.top][entity.left] = character

        return stringify_2d_list(
            render_matrix,
            row_separator="\n",
            column_separator=""
        )
