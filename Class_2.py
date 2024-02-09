class Shape:
    def __init__(self):
        self.areax = 0

    def area(self):
        print(self.areax)


class Square(Shape):
    def __init__(self, a):
        super().__init__()
        self.length = a
        self.area_square = super().area

    def area(self):
        self.area_square = self.length ** 2
        print(self.area_square)