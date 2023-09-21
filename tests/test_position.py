from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    TEST_XYCOORDINATES = (1,1)
    NEW_POSITION = (5,7)

    def test_init(self):
        testobj = Position()
        assert testobj.coordinates[0] == self.TEST_XYCOORDINATES[0]
        assert testobj.coordinates[1] == self.TEST_XYCOORDINATES[1]
