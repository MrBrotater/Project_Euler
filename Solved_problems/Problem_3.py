"""
Problem 3: Largest Prime Factor
----------------------------------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from Working_on.Reuseable_Functions import numpy_primes_up_to_n

import math


def solution():
    x = 600851475143
    n = int(math.sqrt(x))
    primes = numpy_primes_up_to_n(n)
    prime_factors = []
    for prime in primes:
        if x % prime == 0:
            prime_factors.append(prime)
    largest_prime_factor = prime_factors[-1]
    print(largest_prime_factor)
    return
