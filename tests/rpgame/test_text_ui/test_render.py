from rpgame.entities import Player, Wall
from rpgame.text_ui import TextUI


def test_can_render_entities():
    entities_to_render = [
        Wall(0, 0),
        Player(1, 0),
        Wall(2, 0),
    ]
    ui = TextUI("", entities=entities_to_render)

    assert ui.render() == "|@|"