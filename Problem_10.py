"""
Problem 10: Summation of Primes
----------------------------------
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from Reuseable_Functions import numpy_primes_up_to_n
import numpy as np

def solution():
    n = 10
    primes = np.array(numpy_primes_up_to_n(n))
    print(primes)
    sum_of_primes = np.sum(primes)
    print(sum_of_primes)
    return

# my 100% original seive of eratosthenes algorithm would have taken ~15 hrs to solve
# found a more efficient version that utilized numpy arrays instead of lists and
# solution = 1179908154 (incorrect) not sure why