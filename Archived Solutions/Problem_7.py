"""
Problem 7: 10001st Prime
--------------------------------------
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


from Reuseable_Functions import get_cached_primes


def solution():
    primes = get_cached_primes()
    print(primes[10001 - 1])
    return

# First attempt = 104743 (CORRECT) solved in 0.008070399999999991 seconds
# note: I cheated by using over 70000 primes calculated and cached during Problem 3 :)
