from rpgame.entities import Player
from rpgame.text_ui import TextUI


from typing import List, Tuple, Type


def create_ui_with_player(text_map: str) -> Tuple[TextUI, Player]:
    ui = TextUI.from_map(text_map)
    players = filter_object_type(ui.entities, Player)
    
    return ui, players[0]


def filter_object_type(objects: List[object], desired_type: Type) -> List[object]:
    return [o for o in objects if type(o) == desired_type ]