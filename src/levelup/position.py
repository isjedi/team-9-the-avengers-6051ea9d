class Position:
    coordinates: tuple = (0,0)
    xCoordinate: int = 0
    yCoordinate: int = 0

    def _init_(self, coordinates: tuple):
        self.xcoordinate = coordinates[0]
        self.ycoordinate = coordinates[1]
        self.coordinates = (self.xcoordinate, self.ycoordinate)
