'''
Problem 47:

The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 x 7
    15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2^2 x 7 x 23
    645 = 3 x 5 x 43
    646 = 2 x 17 x 19

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
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

#initial guess used to generate lists of primes and composites
guess = 150000

# list of primes up to guess
primes = numpy_primes_up_to_n(guess)

def has_n_prime_factors(x, n, primes):
    count = 0
    for p in primes:
        if p >= x:
            return False
        if x % p == 0:
            count += 1
            if count == 4:
                return True
    return False

solution = False
n = 1

temp_data = []

while not solution:
    if len(temp_data) == 4:
        print(f'solution = {temp_data[0]}')
        solution = True
    else:
        if has_n_prime_factors(n, 4, primes):
            temp_data += [n]
        else:
            temp_data = []
    n += 1

