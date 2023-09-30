from rpgame.entities import Player, Wall
from rpgame.text_ui import TextUI
from tests.rpgame.conftest import create_ui_with_player


def test_with_simple_1D_packed_map():
    entities_to_render = [
        Wall(0, 0),
        Player(1, 0),
        Wall(2, 0),
    ]
    ui = TextUI(room_dimensions=(3, 1), entities=entities_to_render)

    assert ui.render() == "|@|"
    

def test_when_1D_map_is_not_packed():
    entities_to_render = [
        Wall(0, 0),
        Player(2, 0),
        Wall(4, 0)
    ]
    ui = TextUI(room_dimensions=(5, 1), entities=entities_to_render)
    
    assert ui.render() == "| @ |"


def test_when_2D_map_is_not_packed():
    entities_to_render = [
        Wall(0, 0),
        Player(1, 0),
        Wall(2, 0),
        Wall(0, 1),
        Wall(1, 1),
        Wall(2, 1),
    ]
    ui = TextUI(room_dimensions=(3, 2), entities=entities_to_render)
    
    assert ui.render() == (
"""
|@|
|||
"""
    ).strip()
    
    
def test_when_2D_map_is_not_packed():
    entities_to_render = [
        Wall(0, 0),
        Player(2, 0),
        Wall(4, 0),
        Wall(0, 1),
        Wall(2, 1),
        Wall(4, 1),
    ]
    ui = TextUI(room_dimensions=(5, 2), entities=entities_to_render)
    
    assert ui.render() == (
"""
| @ |
| | |
"""
    ).strip()


def test_when_entities_change_position(larger_map):
    ui, player = create_ui_with_player(larger_map)

    player.move(0, 1)

    expected_ui = (
"""
|||||||
|     |
| @   |
|||||||
"""
    ).strip()
    assert ui.render() == expected_ui