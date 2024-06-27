'''
Problem 23:

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of 
the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two 
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum 
of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

# ------------ imports
import numpy as np
from functools import reduce

# ------------- function definitions

def numpy_primes_up_to_n(n: int) -> list:
    """
    very efficient sieve of eratosthenes implementation to find primes up to number n.
    doesn't seem to work for numbers < 8 for some reason.
    """
    if n < 8:
        return [i for i in [2, 3, 5, 7] if i <= n]
    a = np.array(range(3, n, 2))
    for j in range(0, int(round(np.sqrt(n), 0))):  # checks values from 0 to sqrt(n)
        a[(a != a[j]) & (a % a[j] == 0)] = 0  # assigns all multiples of j to 0
        a = a[a != 0]  # removes all the 0 values from the array
    a = [2] + list(a)  # turns everything back into a list, and adds 2 to beginning
    return a

def proper_divisors_of_n(n: int) -> list:
    """ returns a list of the proper divisors (factors) of the number n """
    factors = []
    for i in range (1, int(n**0.5) + 1):
        if n % i == 0:
            factors += [i, n//i]
    return set(factors)

def abundant_nums_up_to_n(n: int) -> list:
    abund_nums = []
    for num in range(1, n):

        factors = proper_divisors_of_n(num)
        s = sum(factors) - num
        Abund = False
        if s > num:
            abund_nums += [num]

    return abund_nums

# ------------- main

upper_limit = 28123
abundant_nums = abundant_nums_up_to_n(upper_limit)
test_nums = set(range(1, upper_limit+1))
list_len = len(abundant_nums)

for x in range(list_len):
    for y in range(x, list_len):
        s = abundant_nums[x] + abundant_nums[y]
        if s in test_nums:
            test_nums.remove(s)

print(sum(test_nums))
