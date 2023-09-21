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

    def test_Move_Direction_East(self):
        map=GameMap()
        currentpos = map.Get_Position()
        newpos=[]
        newpos.append(currentpos[0]+1)
        newpos.append(currentpos[1])
    def test_Move_Direction_West(self):
        map=GameMap()
        currentpos = map.Get_Position()
        newpos=[]
        newpos.append(currentpos[0]-1)
        newpos.append(currentpos[1])
    def test_Move_Direction_North(self):
        map=GameMap()
        currentpos = map.Get_Position()
        newpos=[]
        newpos.append(currentpos[0])
        newpos.append(currentpos[1]+1)
    def test_Move_Direction_South(self):
        map=GameMap()
        currentpos = map.Get_Position()
        newpos=[]
        newpos.append(currentpos[0])
        newpos.append(currentpos[1]-1)


    def test_getTotalPosition(self):
        pass