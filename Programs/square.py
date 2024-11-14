def area(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Input must be a number")
    if a <= 0:
        raise TypeError("Side length must be positive")
    return a ** 2


def perimeter(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Input must be a number")
    if a <= 0:
        raise TypeError("Side length must be positive")
    return 4 * a
