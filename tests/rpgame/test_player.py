import pytest

from rpgame.entities import Gold, Player


@pytest.fixture
def player():
    yield Player(4, 3)


def test_player_can_move(player):
    player.move(1, 2)

    assert (player.left, player.top) == (5, 5)


def test_player_can_move_in_negative_direction(player):
    player.move(-1, -4)

    assert (player.left, player.top) == (3, -1)


def test_player_can_move_only_vertically(player):
    player.move(left=2)

    assert (player.left, player.top) == (6, 3)


def test_player_can_move_only_horizontally(player):
    player.move(top=-2)

    assert (player.left, player.top) == (4, 1)


def test_player_can_pickup_gold(player):
    gold = Gold(4, 3)

    assert not player.inventory

    player.pickup(gold)

    assert player.inventory == [gold]
    
    
def test_player_can_pickup_only_gold_in_same_location(player):
    gold = Gold(1, 1)
    
    with pytest.raises(RuntimeError, match="Cannot pickup item, it's too far away"):
        player.pickup(gold)
