import math


def area(r):
    if not isinstance(r, (int, float)):
        raise TypeError("Input must be a number")
    if r <= 0:
        raise TypeError("Radius must be positive")
    return math.pi * r ** 2


def perimeter(r):
    if not isinstance(r, (int, float)):
        raise TypeError("Input must be a number")
    if r <= 0:
        raise TypeError("Radius must be positive")
    return 2 * math.pi * r
