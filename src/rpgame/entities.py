class Wall:
    def __init__(self, left: float, top: float):
        self.left = left
        self.top = top


class Player:
    def __init__(self, left: float, top: float):
        self.left = left
        self.top = top
    
    def move(self, left: float = 0, top: float = 0) -> None:
        self.left += left
        self.top += top 
    
    
class Emptiness:
    def __init__(self, left: float, top: float):
        self.left = left
        self.top = top