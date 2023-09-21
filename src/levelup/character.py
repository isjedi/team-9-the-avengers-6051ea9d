from levelup.gamemap import GameMap
from levelup.position import Position

class Character:
    name = ""

    def __init__(self, character_name = "Jennifer"):
        self.name = character_name
        self.position = None

    def get_name(self):
        return self.name

    def enter_map(self, map: GameMap):
        return map

    
