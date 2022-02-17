import timeit
import numpy as np

def is_x_a_multiple_of_y(x: int, y: int) -> bool:
    """ returns True if x is a multiple of y, else False """
    return True if x % y == 0 else False


def next_fibonacci_term(n1: int, n2: int) -> int:
    """ returns the next fibonacci term given n1 and n2"""
    return n1 + n2


def find_n_fibonacci_terms(n: int) -> list:
    """ returns the first n fibonacci terms in a list """
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        terms = [1, 2]
        for term in range(3, n + 1):
            terms.append(terms[-1] + terms[-2])
        return terms


def primes_up_to_n(n: int) -> list:
    """
    My first attempt at sieve of eratosthenes, which was quite slow.
    deprecated, now using numpy_primes_up_to_n
    """
    primes = get_cached_primes()
    not_primes = get_not_primes(primes, n)
    start_time = timeit.default_timer()

    if len(primes) > 0 and n < primes[-1]:
        return [prime for prime in primes if prime <= n]

    if len(primes) == 0:
        start_n = 2
    else:
        start_n = primes[-1] + 1

    for num in range(start_n, n + 1):
        if num % 1000 == 0:
            print(f'{num} of {n} complete')
            print(f'execution time = {timeit.default_timer() - start_time} seconds')
            start_time = timeit.default_timer()
            save_primes_to_cache(primes)
        if num not in not_primes:
            primes.append(num)
            new_not_prime = num * num
            while new_not_prime <= n:
                not_primes.append(new_not_prime)
                new_not_prime += num
    save_primes_to_cache(primes)
    return primes


def numpy_primes_up_to_n(n: int) -> list:
    """ very efficient sieve of eratosthenes implementation to find primes up to number n """
    a = np.array(range(3, n, 2))
    for j in range(0, int(round(np.sqrt(n), 0))):  # checks values from 0 to sqrt(n)
        a[(a != a[j]) & (a % a[j] == 0)] = 0  # assigns all multiples of j to 0
        a = a[a != 0]  # removes all the 0 values from the array
    a = [2] + list(a)  # turns everything back into a list, and adds 2 to beginning
    return a


def no_of_proper_divisors(n: int, primes: list) -> int:
    """
    calculates the expected number of proper divisors of number n using prime factorization.
    primes are taken as an input because this was used iteratively for one problem and
    calculating inside the function was extremely slow.  not sure how to make this
    an optional argument yet.
    """
    # primes = numpy_primes_up_to_n(n)
    prime_factors = [p for p in primes if n % p == 0]
    no_factors = 1
    for p in prime_factors:
        count = 0
        while n % p == 0:
            count += 1
            n /= p
        no_factors *= (count + 1)
    return no_factors


def proper_divisors_of_n(n: int) -> list:
    """ returns a list of the proper divisors (factors) of the number n """
    primes = numpy_primes_up_to_n(n)
    prime_factors = [p for p in primes if n % p == 0]
    factors = prime_factors + [int(n / p) for p in prime_factors] + [1, n]
    for p in prime_factors:
        while p <= n:
            p += p
            if p not in factors and n % p == 0:
                factors += [p, int(n / p)]
    return factors


def get_not_primes(primes: list, n: int) -> list:
    """ given a list of primes, calculates numbers that can be confirmed as not primes
    up to number n """
    not_primes = []
    for prime in primes:
        new_not_prime = prime * prime
        while new_not_prime <= n:
            not_primes.append(new_not_prime)
            new_not_prime += prime
    return not_primes


def save_primes_to_cache(primes: list) -> None:
    """
    given a list of primes, checks if any are not already cached, then saves them
    to the cached_primes.json file
    """
    primes = np.array(primes, dtype='int64')
    np.save('../Cache_files/cached_primes.npy', primes)
    return


def get_cached_primes() -> list:
    """ retrieves any primes cached in the cached_primes.json file """
    try:
        primes = np.load('../Cache_files/cached_primes.npy')
        return list(primes)
    except FileNotFoundError:
        return []


def is_palindrome(n: int) -> bool:
    """ returns true if n is a palindrome (same value reversed as forwards) """
    return True if str(n) == str(n)[::-1] else False


def sum_digits(n):  # NOTE: tested this with digits = numpy array and return numpy.sum, was much slower
    """ returns the sum of the digits in a number n """
    digits = [int(i) for i in str(n)]
    return sum(digits)
