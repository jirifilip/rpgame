from typing import Type, List

from rpgame.entities import Wall, Player
from rpgame.text_ui import TextUI
from tests.rpgame.conftest import _create_world_with_player

    
def _filter_object_type(objects: List[object], desired_type: Type):
    return [o for o in objects if type(o) == desired_type   ]
    


def test_player_can_move_right():
    board, player = _create_world_with_player(
"""
|-----|
| @   |
|     |
|-----|
"""
    )
    
    player.move(1)
    player.move(0, 1)
    
    expected_board = (
"""
|-----|
|     |
| @   |
|-----|
"""
    )
    assert board.render() == expected_board    
    
    
def test_text_ui_can_be_initialized_with_map():
    map = (
"""
 _
| |
|@|
|_|
"""        
    )
    
    ui = TextUI.from_map(map)
    
    assert len(ui.entities) == 9
    
    
def test_text_ui_has_correct_entity_counts_when_initialized_with_map():
    map = (
"""
 _
| |
|@|
|_|
"""        
    )
    
    ui = TextUI.from_map(map)
    
    walls = _filter_object_type(ui.entities, Wall)
    players = _filter_object_type(ui.entities, Player)
    assert len(list(walls)) == 8
    assert len(list(players)) == 1    

