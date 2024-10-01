"""
Problem 32:

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is
1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

pandigital_check = set(range(1, 10))

def digits_of_n(n):
    return [int(digit) for digit in str(n)]

def is_pandigital(a, b, c):
    digits = set(digits_of_n(a) + digits_of_n(b) + digits_of_n(c))
    return digits == pandigital_check

print(is_pandigital(123, 456, 789))

# Note: above section is working and probably fast enough, need to solve second half of the problem
