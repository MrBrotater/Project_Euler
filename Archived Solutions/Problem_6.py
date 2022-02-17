"""
Problem 6: Sum Square Difference
--------------------------------------
The sum of the squares of the first ten natural numbers is:

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and
the square of the sum is:

    3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and
the square of the sum.
"""


def sum_of_squares(n):
    temp_sum = 0
    for i in range(1, n + 1):
        temp_sum += i * i
    return temp_sum


def square_of_sum(n):
    temp_sum = 0
    for i in range(1, n + 1):
        temp_sum += i
    return temp_sum * temp_sum


def solution():
    n = 100
    sumsq = sum_of_squares(n)
    sqsum = square_of_sum(n)
    print(sumsq, sqsum, sqsum - sumsq)
    return
