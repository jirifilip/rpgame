from typing import Generic
from typing import List
from typing import Tuple
from typing import Type
from typing import TypeVar

import pytest
from rpgame.entities import Entity
from rpgame.entities import Player
from rpgame.game import Game
from rpgame.room import Room


T = TypeVar("T", bound=Entity)


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


def create_game(text_map: str) -> Tuple[Room, Game]:
    room = Room.from_text_map(text_map)

    players = filter_entity_type(room.entities, Player)
    player_facade = Game(players[0], room.entities)

    return room, player_facade


def assert_entities_are_same_by_location(actual_entities: List[Entity], expected_entities: List[Entity]):
    """Compares expected entities with actual entities by their location"""
    for actual, expected in zip(actual_entities, expected_entities):
        assert (actual.left, actual.top) == (expected.left, expected.top)


def filter_entity_type(objects: List[Entity], desired_type: Type[T]) -> List[T]:
    return [o for o in objects if type(o) == desired_type ]
