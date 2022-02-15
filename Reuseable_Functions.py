import math
import numpy

def is_x_a_multiple_of_y(x: int, y: int) -> bool:
    """ returns True if x is a multiple of y, else False """
    return True if x % y == 0 else False


def next_fibonacci_term(n1, n2):
    """ returns the next fibonacci term given n1 and n2"""
    return n1 + n2


def find_n_fibonacci_terms(n):
    """
    returns the first n fibonacci terms in a list
    """
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        terms = [1, 2]
        for term in range(3, n + 1):
            terms.append(terms[-1] + terms[-2])
        return terms


def primes_up_to_n(n):
    """ returns all primes up to number n using sieve of eratosthenes method"""
    primes = []
    not_primes = []
    for num in range(2, n + 1):
        if num % 1000 == 0:
            print(f'{num} of {n} complete')
        if num in not_primes:
            pass
        else:
            primes.append(num)
            new_not_prime = num * num
            while new_not_prime <= n:
                not_primes.append(new_not_prime)
                new_not_prime += num
    print(primes)
    return primes
