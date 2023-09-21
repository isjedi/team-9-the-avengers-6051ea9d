from levelup.gamemap import GameMap
from levelup.position import Position

class Character:
    name = ""
    position = None
    map = None

    def __init__(self, character_name = "Jennifer"):
        self.name = character_name
        self.position = None
        self.map = None

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def enter_map(self, map: GameMap):
        self.map = map
        return map
    
    def move(self, direction):
        if self.position is None:
            raise ValueError('character position never set')
        else:
            map.calculatePosition(self.position, direction)
        