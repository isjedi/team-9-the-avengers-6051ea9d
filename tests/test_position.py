from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    TEST_XYCOORDINATES: list = [1,1]
    NEW_POSITION_X: int = 5
    NEW_POSITION_Y: int = 7

    def test_init_xcoordinate(self):
        TEST_XYCOORDINATES = [1,1]
        testobj1 = Position(TEST_XYCOORDINATES)
        assert testobj1.coordinates[0] == self.TEST_XYCOORDINATES[0]

    def test_init_ycoordinate(self):
        TEST_XYCOORDINATES = [1,1]
        testobj2 = Position(TEST_XYCOORDINATES)
        assert testobj2.coordinates[1] == self.TEST_XYCOORDINATES[1]

    def test_Position_xcoordinate(self):
        TEST_XYCOORDINATES = [1,1]
        NEW_POSITION_X = 5
        NEW_POSITION_Y = 7
        testobj3 = Position(TEST_XYCOORDINATES)
        testobj3.setPosition(NEW_POSITION_X, NEW_POSITION_Y)
        assert testobj3.coordinates[0] == NEW_POSITION_X

    def test_Position_ycoordinate(self):
        TEST_XYCOORDINATES = [1,1]
        NEW_POSITION_X = 6
        NEW_POSITION_Y = 8
        testobj3 = Position(TEST_XYCOORDINATES)
        testobj3.setPosition(NEW_POSITION_X, NEW_POSITION_Y)
        assert testobj3.coordinates[1] == NEW_POSITION_Y
