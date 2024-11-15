'''
Problem 46:

It was proposed by Christian Goldbach that every composite number can be written as the sum of a prime and twice a square.

    9 = 7 + 2 x 1^2
    15 = 7 + 2 x 2^2
    21 = 3 + 2 x 3^2
    25 = 3 + 2 x 3^2
    27 = 19 + 2 x 2^2
    33 = 31 + 2 x 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
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
guess = 6000

# list of primes up to guess
primes = numpy_primes_up_to_n(guess)

# list of doubled square values up to sqrt(guess)
twice_squares = []

i = 1
n = 2 * (i **2)
while n < guess:
    twice_squares += [n]
    i += 1
    n = 2 * (i **2)

# list of numbers up to guess that conform to goldbachs conjecture

goldbachs = []
for prime in primes:
    for square in twice_squares:
        n = prime + square
        if n not in goldbachs:
            goldbachs += [n]

# list of odd composite numbers to test
odd_composites = []

for i in range(3, guess):
    if i % 2 != 0:
        if i not in primes:
            odd_composites += [i]

solution = False
i = 0

while not solution:
    comp = odd_composites[i]
    if comp not in goldbachs:
        print(f'solution = {comp}')
        solution = True
    i += 1
