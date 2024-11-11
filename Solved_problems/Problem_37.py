'''
Problem 37:

The number 3797 has an interesting property.  Being prime itself, it is possible to 
continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7.  Simililarly we canwork from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right
and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

'''
Analysis:
Primes have to end in the numbers 1, 3, 7, or 9 

Assumption above incorrectly excludes 23 and 53, adjusted the truncatable_candidates
generator to include all 2-digit primes
'''

import numpy as np

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

primes = numpy_primes_up_to_n(1000000)

good_numbers = {'1', '3', '7', '9'}

truncatable_candidates = []

for prime in primes:
    digits = set(str(prime))
    if len(digits) < 2:
        pass
    elif len(digits) == 2:
        truncatable_candidates += [prime]
    elif len(digits.difference(good_numbers)) == 0:
        truncatable_candidates += [prime]

def is_truncatable(n):
    forward = str(n)
    reverse = forward[::-1]
    for i in range(len(forward)):
        if int(forward) not in primes:
            return False
        if int(reverse[::-1]) not in primes:
            return False
        forward = forward[:-1]
        reverse = reverse[:-1]

    return True

solution = 0

for prime in truncatable_candidates:
    if is_truncatable(prime):
        solution += prime

print(solution)

# expected results = 748317
# the highest prime that exists is 739397
