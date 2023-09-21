class Position:
    coordinates: tuple = (0, 0)
    # random ints in a bound range of 0-9 use random.randint(0,9)

    def _init_(self, coordinates: tuple):
        self.xcoordinate = coordinates[0]
        self.ycoordinate = coordinates[1]
        self.coordinates = (self.xcoordinate, self.ycoordinate)

    def Position():
        self.coordinates = coordinates
