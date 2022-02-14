"""
Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from Reuseable_Functions import is_x_a_multiple_of_y


def solution():
    n = 1000
    sum_of_factors = 0
    for i in range(1, n):
        if is_x_a_multiple_of_y(i, 3):
            sum_of_factors += i
            print(f'{i} is a multiple of 3')
        elif is_x_a_multiple_of_y(i, 5):
            sum_of_factors += i
            print(f'{i} is a multiple of 5')
        else:
            print(f'{i} is a NOT multiple of 3 or 5')
    print(sum_of_factors)

# first attempt = 33165 (WRONG)
# second attempt = 233168 (CORRECT)
