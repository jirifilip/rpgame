from rpgame.entities import Player
from rpgame.text_ui import TextUI


from typing import Tuple


def _create_world_with_player(initial_state: str) -> Tuple[TextUI, Player]:
    player = Player(0, 0)
    board = TextUI(initial_state, entities=[player])
    return board, player