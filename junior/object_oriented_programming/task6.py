# Class hierarchy for Shape, Square, and Triangle with area() method

# Solution 1 (Basic inheritance)

class Shape:
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Solution 2 (Using `super()` for shared attributes):

class Shape2:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Square2(Shape2):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle2(Shape2):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

