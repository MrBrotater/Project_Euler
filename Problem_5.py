"""
Problem 5: Smallest Multiple
--------------------------------------
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def solution():
    n = 20
    factors = range(1, 20)
    while True:
        remainder = 0

        if n % 1000000 == 0:
            print(f'checking {n}')

        for factor in factors:
            remainder += n % factor

        if remainder == 0:
            return print(f'the solution is {n}')

        n += 1

    return


# First solution = 232792560 (CORRECT) solved in 237.19471109999998 seconds
