from rpgame.entities import Player
from rpgame.text_ui import TextUI


from typing import List, Tuple, Type


def create_world_with_player(initial_state: str) -> Tuple[TextUI, Player]:
    player = Player(0, 0)
    board = TextUI(initial_state, entities=[player])
    return board, player


def filter_object_type(objects: List[object], desired_type: Type):
    return [o for o in objects if type(o) == desired_type   ]