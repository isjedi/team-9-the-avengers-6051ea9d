class Position:
    coordinates: list = [0,0]
    # random ints in a bound range of 0-9 use random.randint(0,9)

    def __init__(self, coordinates: list):
        self.coordinates = coordinates #(self.xcoordinate, self.ycoordinate)

    def setPosition(self, xCoordinates, yCoordinates):
        self.coordinates[0] = xCoordinates
        self.coordinates[1] = yCoordinates

    def __str__(self):
        return f"coords: {self.coordinates}"