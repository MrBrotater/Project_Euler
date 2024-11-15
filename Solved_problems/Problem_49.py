'''
Problem 49:

The arithmetic sequence, 1487, 4871, 8147, in which each of the terms increases by 3330, is unusual in two ways:

    (i) each of the three terms are prime
    (ii) each of the 4-digit numbers ar permutations of one another

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there
is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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

# generate all of the 4 digit primes
primes = [p for p in numpy_primes_up_to_n(10000) if p > 1000]

# segregate primes that conform to the arithmetic sequence [n, n + 3330, n + 2 * 3330]

def test1(primes):
    output = []
    for p in primes:
        p2 = p + 3330
        if p2 in primes:
            p3 = p + 2 * 3330
            if p3 in primes:
                output += [[p, p2, p3]]
    return output

arithmetic_series = test1(primes)

def find_permutations(s):  
    # recursive function to compute permutations found online, not original
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i, c in enumerate(s):
            for perm in find_permutations(s[:i] + s[i+1:]):
                perms.append(c + perm)
        return perms

solutions = []

for series in arithmetic_series:
    series = [str(x) for x in series]
    perms = find_permutations(series[0])
    if str(series[1]) in perms:
        if series[2] in perms:
            solution = series[0] + series[1] + series[2]
            solutions += [solution]

print(solutions)
