class GameMap:
    def __init__(self):
        self.init_number = 100

    def Get_Position(self):
        default_coordinates: list = [4,3]
        xcoordinate = default_coordinates[0]
        ycoordinate = default_coordinates[1]
        coordinates = (xcoordinate, ycoordinate)
        return coordinates





if __name__ == '__main__':
    map=GameMap()
    position=map.Get_Position()
    print(position[1])




