import pytest

from rpgame.entities import Entity, Player
from rpgame.text_ui import TextUI

from typing import List, Tuple, Type

from rpgame.game import Game



def create_game(text_map: str) -> Tuple[TextUI, Game]:
    ui = TextUI.from_map(text_map)

    players = filter_entity_type(ui.entities, Player)
    player_facade = Game(players[0], ui.entities)
    
    return ui, player_facade


def filter_entity_type(objects: List[Entity], desired_type: Type) -> List[Entity]:
    return [o for o in objects if type(o) == desired_type ]


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


def assert_entities_are_same_by_location(actual_entities: List[Entity], expected_entities: List[Entity]):
    """Compares expected entities with actual entities by their location"""
    for actual, expected in zip(actual_entities, expected_entities):
        assert (actual.left, actual.top) == (expected.left, expected.top)