from rpgame.entities import Wall


def test_wall_has_location_properties():
    wall = Wall(2, 1)

    assert wall.left == 2
    assert wall.top == 1
