import pytest

from rpgame.entities import Wall, Player
from rpgame.text_ui import TextUI
from tests.rpgame.conftest import filter_object_type


@pytest.fixture
def larger_map():
    yield (
"""
|||||||
| @   |
|     |
|||||||
"""
    )
    
    
@pytest.fixture
def small_map():
    yield (
"""
|||
| |
|@|
|||
"""   
    )
    
    
def test_can_be_initialized(small_map):
    ui = TextUI.from_map(small_map)
    
    assert len(ui.entities) == 11
    
    
def test_has_correct_entity_counts(small_map):
    ui = TextUI.from_map(small_map)
    
    walls = filter_object_type(ui.entities, Wall)
    players = filter_object_type(ui.entities, Player)
    assert len(list(walls)) == 10
    assert len(list(players)) == 1    


def test_player_has_correct_position(small_map):
    ui = TextUI.from_map(small_map)
    
    all_players = filter_object_type(ui.entities, Player)
    assert len(all_players) == 1
    
    player = all_players[0]
    assert (player.left, player.top) == (1, 2)
    

def test_small_map_has_correct_room_dimensions(small_map):
    ui = TextUI.from_map(small_map)
    
    assert ui.room_dimensions == (3, 4)