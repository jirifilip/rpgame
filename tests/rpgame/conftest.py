import pytest

from rpgame.entities import Entity, Player
from rpgame.text_ui import TextUI

from typing import List, Tuple, Type


def create_ui_with_player(text_map: str) -> Tuple[TextUI, Player]:
    ui = TextUI.from_map(text_map)
    players = filter_object_type(ui.entities, Player)
    
    return ui, players[0]


def filter_object_type(objects: List[object], desired_type: Type) -> List[object]:
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