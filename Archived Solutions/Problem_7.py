"""
Problem 7: 10001st Prime
--------------------------------------
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


from Reuseable_Functions import numpy_primes_up_to_n


def solution():
    primes = numpy_primes_up_to_n(105000)
    print(primes[10001 - 1])
    return

# First attempt = 104743 (CORRECT) solved in 0.02725340000000001 seconds
