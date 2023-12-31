from rpgame.entities import Player, Wall
from rpgame.room import Room
from rpgame.text_ui import TextUI
from tests.rpgame.conftest import create_game


def test_with_simple_1D_packed_map():
    entities_to_render = [
        Wall(0, 0),
        Player(1, 0),
        Wall(2, 0),
    ]
    room = Room(dimensions=(3, 1), entities=entities_to_render)

    assert TextUI.render(room) == "|@|"


def test_when_1D_map_is_not_packed():
    entities_to_render = [Wall(0, 0), Player(2, 0), Wall(4, 0)]
    room = Room(dimensions=(5, 1), entities=entities_to_render)

    assert TextUI.render(room) == "| @ |"


def test_when_2D_map_is_packed():
    entities_to_render = [
        Wall(0, 0),
        Player(1, 0),
        Wall(2, 0),
        Wall(0, 1),
        Wall(1, 1),
        Wall(2, 1),
    ]
    room = Room(dimensions=(3, 2), entities=entities_to_render)

    assert (
        TextUI.render(room)
        == (
            """
|@|
|||
"""
        ).strip()
    )


def test_when_2D_map_is_not_packed():
    entities_to_render = [
        Wall(0, 0),
        Player(2, 0),
        Wall(4, 0),
        Wall(0, 1),
        Wall(2, 1),
        Wall(4, 1),
    ]
    room = Room(dimensions=(5, 2), entities=entities_to_render)

    assert (
        TextUI.render(room)
        == (
            """
| @ |
| | |
"""
        ).strip()
    )


def test_when_entities_change_position(larger_map):
    room, game = create_game(larger_map)

    game.move_player(0, 1)

    expected_room = (
        """
|||||||
|     |
| @   |
|||||||
"""
    ).strip()
    assert TextUI.render(room) == expected_room
