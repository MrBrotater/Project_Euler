"""
Problem 16: Power Digit Sum
----------------------------------
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def sum_digits(n):
    digits = [int(i) for i in str(n)]
    return sum(digits)


def solution():
    print(sum_digits(2**1000))
    return
