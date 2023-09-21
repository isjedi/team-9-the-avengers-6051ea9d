from unittest import TestCase
from levelup.gamemap import GameMap

class TestGameGetPosition(TestCase):
    def test_init(self):
        map = GameMap()
        num = map.init_number
        assert num != None

    def test_Get_xPosition(self):
        map = GameMap()
        testpos = map.Get_Position()
        assert testpos[0] != 5

    def test_Get_yPosition(self):
        map = GameMap()
        testpos = map.Get_Position()
        assert testpos[1] != 4

    # def test_Get_Position(self):
    #     map = GameMap()
    #     yposition = map.Get_Position
    #     assert yposition != None

    # def test_CalculatePosition(self):
        
    #     pass

    # def test_getTotalPosition(self):
    #     pass