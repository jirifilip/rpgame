import pytest
from rpgame.text_ui import TextUI

from tests.rpgame.conftest import create_game


@pytest.fixture
def simple_text_map():
    yield (
"""
| @ o |
"""
    ).strip()


def test_when_player_collides_with_an_item__it_ends_up_in_his_inventory(simple_text_map):
    _, game = create_game(simple_text_map)

    assert not game.player_inventory

    game.move_player(left=1)
    assert not game.player_inventory

    game.move_player(left=1)
    assert len(game.player_inventory) == 1


def test_when_player_picks_up_an_item__it_disapperas_from_the_room(simple_text_map):
    room, game = create_game(simple_text_map)

    game.move_player(left=1)
    game.move_player(left=1)
    game.move_player(left=1)

    expected_ui = (
"""
|    @|
"""
    ).strip()
    assert TextUI.render(room) == expected_ui
