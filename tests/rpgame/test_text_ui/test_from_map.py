import pytest

from rpgame.entities import Wall, Player
from rpgame.text_ui import TextUI
from tests.rpgame.conftest import create_ui_with_player, filter_object_type


@pytest.fixture
def larger_map():
    yield (
"""
|-----|
| @   |
|     |
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
    ui, player = create_ui_with_player(larger_map)
    
    player.move(1)
    player.move(0, 1)
    
    expected_ui = (
"""
|-----|
|     |
| @   |
|-----|
"""
    )
    assert ui.render() == expected_ui    
    
    
def test_can_be_initialized(larger_map):
    ui = TextUI.from_map(larger_map)
    
    assert len(ui.entities) == 9
    
    
def test_has_correct_entity_counts(small_map):
    ui = TextUI.from_map(small_map)
    
    walls = filter_object_type(ui.entities, Wall)
    players = filter_object_type(ui.entities, Player)
    assert len(list(walls)) == 8
    assert len(list(players)) == 1    


def test_player_has_correct_position(small_map):
    ui = TextUI.from_map(small_map)
    
    all_players = filter_object_type(ui.entities, Player)
    assert len(all_players) == 1
    
    player = all_players[0]
    assert (player.left, player.top) == (1, 2)
    
