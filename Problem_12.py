"""
Problem 12: Highly Divisible Triangular Number
----------------------------------
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import numpy as np
from Reuseable_Functions import numpy_primes_up_to_n, number_of_factors
from Reuseable_Functions import save_primes_to_cache, get_cached_primes


def solution():
    tri_num = 63839350
    n = 11300
    max_factors = 0

    primes = get_cached_primes()
    if len(primes) == 0:
        primes = numpy_primes_up_to_n(80000000)
        save_primes_to_cache(primes)
    print(primes)
    while max_factors <= 500:
        num_factors = number_of_factors(tri_num, [p for p in primes if p < tri_num])
        if num_factors > max_factors:
            max_factors = num_factors
            print(f'triangular number {tri_num} has the new max factors of {max_factors}')
        tri_num += n
        n += 1
        if n % 100 == 0:
            print(f'progress: n = {n}, tri_num = {tri_num}')
    return

# solution = 76576500, need to find a way to get there in a reasonable time

# stopped with progress: n = 11300, tri_num = 63839350