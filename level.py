class Level:

    def __init__(self,bricks_coordinates):

        self.bricks_coordinates = bricks_coordinates

    def add_a_brick(self,brick_coordinates):

        self.bricks_coordinates.append(brick_coordinates)

    def __getitem__(self,i):

        return self.bricks_coordinates[i]

    def __setitem__(self,i,coordinates):

        self.bricks_coordinates[i] = coordinates

    def __delitem__(self,i):

        self.bricks_cordinates[i] = None
