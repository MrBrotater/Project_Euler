"""
Problem 5: Smallest Multiple
--------------------------------------
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def solution():
    solution_found = False
    n = 20
    factors = range(1, 10)
    print(factors)
    while not solution_found:
        switch = 1

        for factor in factors:
            print(n % factor)
            if n % factor != 0:
                break

        n += 1

    return None
