from tests.rpgame.conftest import create_game


def test_when_player_collides_with_an_item__it_ends_up_in_his_inventory():
    _, game =  create_game(
"""
| @ o |
"""
    )
    
    assert not game.player_inventory
    
    game.move_player(left=1)
    assert not game.player_inventory
    
    game.move_player(left=1)
    assert len(game.player_inventory) == 1
