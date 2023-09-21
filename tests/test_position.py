from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    TEST_XYCOORDINATES = (10,10)
    NEW_POSITION = (5,5)

    def test_init(self):
        TEST_XYCOORDINATES = (1,1)
        testobj = Position()
        assert testobj.coordinates[0] == self.TEST_XYCOORDINATES[0]
        assert testobj.coordinates[1] == self.TEST_XYCOORDINATES[1]

    def test_set_position(self):
        testobj = Position()
        