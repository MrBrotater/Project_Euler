"""
Problem 35:

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, 719, are
themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97

How many circular primes are there below one million?
"""

"""
Thoughts:

after some experimentation it eventually became apparent that all of the circular primes
(excluding the single digit primes 2, 3, 5, & 7) are made up of only the digits 1, 3, 7, and 9.
This can be used to speed up the solution by focusing on primes containing these digits.
"""

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

# eliminate any primes containing 0, 2, 4, 5, 6, & 8
bad_digits = ['0', '2', '4', '5', '6', '8']

def no_bad_digits(n, bad_digits):
    for digit in str(n):
        if digit in bad_digits:
            return False
    return True

potential_circ_primes = []
for prime in primes:
    if no_bad_digits(prime, bad_digits):
        potential_circ_primes += [prime]

def get_rotations(n):
    rotations = [n]

    n = str(n)
    n_length = len(n)

    for rotation in range(1, n_length):
        n = n[1:n_length] + n[0]
        rotations += [int(n)]

    return rotations

circular_primes = [2, 5]  #2 & 5 are excluded by the bad digit check but are circular due to being single digit

for prime in potential_circ_primes:
    if prime not in circular_primes:
        rotations = get_rotations(prime)
        is_circular = True
        for rotation in rotations:
            if rotation not in primes:
                is_circular = False
                break
        if is_circular:
            circular_primes += rotations

print(len(set(circular_primes)))
