"""
Euler discovered the remarkable quadratic formula:

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41,
41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive
values 0 <= n <= 79.  The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n^2 + an + b, were abs(a) < 1000 and abs(b) <= 1000

    where abs(n) is the modulus/absolute value of n (e.g. abs(11) = 11 and abs(-4) = 4)

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number
of primes for consecutive values of n, starting with n = 0.
"""

"""
My thoughts:
1) b MUST be a prime number for n = 0 to produce a prime number
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

primes = numpy_primes_up_to_n(60000)
# print(primes)

def compute_quadratic(n, a, b):
    return n*n + a*n + b

max_n = 0
max_a = 0
max_b = 0

for b in numpy_primes_up_to_n(1000):
    for a in range(-1000, 1000):
        n = 0
        formula_holds = True
        while formula_holds:
            if n*n + a*n + b in primes:
                n += 1
            else:
                if n > max_n:
                    max_n = n
                    max_a = a
                    max_b = b
                # print(f'a = {a}, b = {b}, num solutions = {n}')
                formula_holds = False

print(max_n, max_a, max_b, max_a*max_b)

# expected_answer = -59231
