class Position:
    xCoordinate: int = 0
    yCoordinate: int = 0

    def _init_(self, xycoordinates: tuple):
        self.xcoordinate = xycoordinates[0]
        self.ycoordinate = xycoordinates[1]
        self.xycoordinates = (self.xcoordinate, self.ycoordinate)
