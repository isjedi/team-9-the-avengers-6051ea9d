class Position:
    coordinates: tuple = (1,1)
    xCoordinate: int = 1
    yCoordinate: int = 1

    def _init_(self, coordinates: tuple):
        self.xcoordinate = coordinates[0]
        self.ycoordinate = coordinates[1]
        self.coordinates = (self.xcoordinate, self.ycoordinate)
