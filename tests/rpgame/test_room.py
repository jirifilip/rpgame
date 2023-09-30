from rpgame.entities import Wall, Player
from rpgame.room import Room
from tests.rpgame.conftest import (
    assert_entities_are_same_by_location, 
    filter_entity_type
)


def test_has_correct_amount_of_entities(small_map):
    room = Room.from_text_map(small_map)
    
    assert len(room.entities) == 11
 
 
def test_creates_correct_entities():
    text_map = (
"""
|||
|@|
| |
"""
    ).strip()
    room = Room.from_text_map(text_map)
    
    expected_entities = [
        Wall(0, 0), Wall(1, 0), Wall(2, 0),
        Wall(0, 1), Player(1, 1), Wall(2, 1),
        Wall(0, 2), Wall(2, 2)
    ]
    assert_entities_are_same_by_location(room.entities, expected_entities)
    
    
def test_has_correct_entity_counts(small_map):
    room = Room.from_text_map(small_map)
    
    walls = filter_entity_type(room.entities, Wall)
    players = filter_entity_type(room.entities, Player)
    assert len(list(walls)) == 10
    assert len(list(players)) == 1    


def test_player_has_correct_position(small_map):
    room = Room.from_text_map(small_map)
    
    all_players = filter_entity_type(room.entities, Player)
    assert len(all_players) == 1
    
    player = all_players[0]
    assert (player.left, player.top) == (1, 2)
    

def test_small_map_has_correct_room_dimensions(small_map):
    room = Room.from_text_map(small_map)
    
    assert room.dimensions == (3, 4)