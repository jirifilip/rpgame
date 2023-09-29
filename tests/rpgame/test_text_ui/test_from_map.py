import pytest

from rpgame.entities import Wall, Player
from rpgame.text_ui import TextUI
from tests.rpgame.conftest import create_world_with_player, filter_object_type


@pytest.fixture
def larger_map():
    yield (
"""
|-----|
| @   |
|     |W
|-----|
"""
    )
    
    
@pytest.fixture
def small_map():
    yield (
"""
 _
| |
|@|
|_|
"""   
    )

    
def test_player_can_move_right(larger_map):
    board, player = create_world_with_player(larger_map)
    
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
    
    
def test_can_be_initialized(larger_map):
    ui = TextUI.from_map(larger_map)
    
    assert len(ui.entities) == 9
    
    
def test_has_correct_entity_counts(small_map):
    ui = TextUI.from_map(small_map)
    
    walls = filter_object_type(ui.entities, Wall)
    players = filter_object_type(ui.entities, Player)
    assert len(list(walls)) == 8
    assert len(list(players)) == 1    


def test_entities_have_correct_positions():
    pass