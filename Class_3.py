class Shape:
    def __init__(self):
        self.areax = 0

    def area(self):
        if isinstance(self, Square):
            print(self.length ** 2)
        elif isinstance(self, Rectangle):
            print(self.length * self.width)
        else:
            print(self.areax)


class Square(Shape):
    def __init__(self, a):
        super().__init__()
        self.length = a


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.length = a
        self.width = b