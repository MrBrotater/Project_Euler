"""
Problem 30:

Suprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 5^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum, it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits
"""

"""
My Thoughts:
1) The numbers MUST be made of the fifth power of digits 1 - 9  # there should be a way to narrow the solution pool using this info
2) There sould be a way to logically determine an upper limit for n, but it was fast enough to brute force that I didn't bother
"""


def digits_of_n(n):
    return [int(digit) for digit in str(n)]

def sum_of_powers(power, n):
    digits = digits_of_n(n)
    return sum([digit**power for digit in digits])

"""
# Tests
print(sum_of_powers(4, 1634) == 1634)
print(sum_of_powers(4, 8208) == 8208)
print(sum_of_powers(4, 9474) == 9474)
"""

solution = 0
power = 5

for n in range(2, 200000):
    if n == sum_of_powers(power, n):
        print(n, sum_of_powers(power, n))
        solution += n

print(f'solution = {solution}')
