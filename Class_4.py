from math import sqrt


class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def show(self):
        print(self.coordinates)

    def dist(self, another_point):
        s = 0
        for i in range(2):
            s += (self.coordinates[i] - another_point[i])**2
        return sqrt(s)

    def move(self, new_coordinates):
        self.coordinates = new_coordinates