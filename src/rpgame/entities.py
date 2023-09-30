class Wall:
    def __init__(self, left: float, top: float):
        self.left = left
        self.top = top


class Player:
    def __init__(self, left: float, top: float):
        self.left = left
        self.top = top
    
    def move(self, relative_left: float = 0, relative_top: float = 0) -> None:
        pass
    
    
class Emptiness:
    def __init__(self, left: float, top: float):
        self.left = left
        self.top = top