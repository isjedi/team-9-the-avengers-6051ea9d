from unittest import TestCase
from levelup.position import position

class TestPosition(TestCase):
    def test_init(self):
        TEST_XYCOORDINATES = (1,1)
        testobj = Position()
        self.assert = (TEST_XYCOORDINATES[0], testobj.xyCoordinates[0])
        self.assert = (TEST_XYCOORDINATES[1], testobj.xyCoordinates[1])
        