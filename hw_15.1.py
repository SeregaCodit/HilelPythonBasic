from math import sqrt
from math import e


class Rectangle:

    def __init__(self, width, height, accuracy=1e-9):
        self.width = width
        self.height = height
        self.accuracy = accuracy

    def get_square(self):
        res = self.width * self.height
        if all((isinstance(res, float), round(res) - res <= self.accuracy)):
            res = round(res)
        return res

    @staticmethod
    def calc_sides(rectangles: tuple, multiplier=None):
        total_squre = 0
        rect_proportions = 0
        # if all((len(rectangles) == 1, multipliyer is not None)):

        for rect in rectangles:
            rect_proportions += (rect.width / rect.height)
            total_squre += rect.get_square() if not multiplier else rect.get_square() * multiplier
        mean_proportion = rect_proportions / len(rectangles)
        side_b = sqrt(total_squre / mean_proportion)
        side_a = mean_proportion * side_b
        return side_a, side_b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        raise TypeError(f"{other.__name__} must be a Rectangle type!")

    def __add__(self, other):
        if isinstance(other, Rectangle):
            side_a, side_b = Rectangle.calc_sides((self, other))
            return Rectangle(side_a, side_b)
        raise TypeError(f"{other.__name__} must be a Rectangle type!")

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            side_a, side_b = Rectangle.calc_sides((self,), multiplier=n)
            return Rectangle(side_a, side_b)
        raise ValueError(f"The multipliyer must be int(), or float! Got {type(n)}!")

    def __str__(self):
        return f"Rectangle: width: {self.width}, height: {self.height}, square: {self.get_square()}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
