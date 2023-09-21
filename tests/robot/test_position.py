from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    TEST_XYCOORDINATES = (1,1)

    def test_init(self):
        TEST_XYCOORDINATES = (1,1)
        testobj = Position()
        assert testobj.coordinates[0] == self.TEST_XYCOORDINATES[0]
        assert testobj.coordinates[1] == self.TEST_XYCOORDINATES[1]
        