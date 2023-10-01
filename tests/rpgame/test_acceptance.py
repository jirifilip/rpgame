import pytest

from rpgame.text_ui import TextUI
from tests.rpgame.conftest import create_game


@pytest.fixture
def simple_text_map():
    yield "| @ o |"


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

    assert TextUI.render(room) == "|    @|"


def test_player_cannot_move_horizontally_across_a_wall():
    room, game = create_game("|  @|")

    game.move_player(left=1)

    assert TextUI.render(room) == "|  @|"


def test_player_cannot_move_vertically_across_a_wall():
    room, game = create_game(
        """
|||
| |
|@|
|||
                             """.strip()
    )

    game.move_player(top=1)

    expected_ui = (
        """
|||
| |
|@|
|||
        """
    ).strip()
    print(room)
    assert TextUI.render(room) == expected_ui
