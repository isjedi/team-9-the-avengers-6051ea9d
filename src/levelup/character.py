from levelup.gamemap import GameMap

class Character:
    name = ""

    def __init__(self, character_name = "Jennifer"):
        self.name = character_name

    def get_name(self):
        return self.name

    def enter_map(self):
        map = GameMap()
        map_position = map.GetPosition()
        return map_position
