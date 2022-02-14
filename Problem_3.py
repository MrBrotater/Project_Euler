"""
Problem 3: Largest Prime Factor
----------------------------------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from Reuseable_Functions import is_prime


def solution():
    primes = []
    checked = []
    for i in range(600851475143):
        print(i)
        print(is_prime(i, checked))
    #     i_is_prime = result[0]
    #     checked = result[1]
    #     if i_is_prime:
    #         primes.append(i)
    # print(primes)
    return
