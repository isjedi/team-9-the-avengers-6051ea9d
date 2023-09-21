from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    TEST_XYCOORDINATES = (1,1)
    NEW_POSITION = (5,7)

    def test_init(self):
        testobj = Position()
        assert testobj.coordinates[0] == self.TEST_XYCOORDINATES[0]
        assert testobj.coordinates[1] == self.TEST_XYCOORDINATES[1]

    def test_pass(self):
        testobj = Position(NEW_POSITION)
        assert testobj.coordinates[0] == self.NEW_POSITION[0]
        assert testobj.coordinates[1] == self.NEW_POSITION[1]

    def test_set_position(self):
        testobj = Position.Position(self.NEW_POSITION)
        assert testobj[0] == 5
        