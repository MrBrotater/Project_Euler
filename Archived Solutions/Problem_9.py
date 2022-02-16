"""
Problem 9: Special Pythagorean Triplet
--------------------------------------
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:

    a^2 + b^2 = c^2

For example:

    3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    if a < b < c:
        return True if a * a + b * b == c * c else False
    else:
        return False


def solution():
    for x in range(1, 1000):
        for y in range(x + 1, 1000 - x):
            z = 1000 - x - y
            print(x, y, z)
            if x + y + z == 1000:
                if is_pythagorean_triplet(x, y, z):
                    return print('solution: ', x, y, z, x * y * z)
    return

# First attempt = 31875000 (CORRECT) solved in 2.2106484 seconds
