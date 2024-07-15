from functools import wraps


def normalize_fractions(func):
    @wraps(func)
    def wrapper(self, other):
        if self.b == other.b:
            return func(self, other)
        else:
            den = Fraction.get_denominator(self, other)
            self.a = int(self.a * (den / self.b))
            other.a = int(other.a * (den / other.b))
            self.b = other.b = den
            return func(self, other)
    return wrapper


def type_check(func):
    @wraps(func)
    def wrapper(self, other):
        if isinstance(other, Fraction):
            return func(self, other)
        else:
            raise TypeError(f"Value must be Fraction, got {type(other)}")
    return wrapper


class Fraction:
    def __init__(self, a, b, simplify=False):
        self.a = a
        self.b = b
        self.simplify = simplify

    @staticmethod
    def get_denominator(self, other):
        return self.b * other.b if self.b != other.b else self.b

    @type_check
    def __mul__(self, other):
        denominator = self.get_denominator(self, other)
        return Fraction(self.a * other.a, denominator)

    @type_check
    def __add__(self, other):
        denominator = self.get_denominator(self, other)
        return Fraction(int(self.a * (denominator / self.b) + other.a * (denominator / other.b)), denominator)

    @type_check
    def __sub__(self, other):
        denominator = self.get_denominator(self, other)
        return Fraction(int(self.a * (denominator / self.b) - other.a * (denominator / other.b)), denominator)

    @type_check
    @normalize_fractions
    def __eq__(self, other):
        return self.a == other.a

    @type_check
    @normalize_fractions
    def __gt__(self, other):
        return self.a > other.a

    @type_check
    @normalize_fractions
    def __lt__(self, other):
        return self.a < other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')