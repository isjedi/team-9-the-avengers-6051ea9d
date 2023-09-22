from levelup.gamemap import GameMap
from levelup.character import Character
from levelup.controller import Direction
from levelup.position import Position

class FakeCharacter():

    is_moved_called = False
    is_map_entered = False
    current_position = None
    last_move_direction = None

    def __init__():
        self.current_position = Position(5,5)
    
    def enter_map(self, map: GameMap):
        self.is_map_entered = True
        return self.is_map_entered
    
    def move(self, direction: Direction):
        self.is_moved_called = True
        self.last_move_direction = direction
        return self.is_moved_called
