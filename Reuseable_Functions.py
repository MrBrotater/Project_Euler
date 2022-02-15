
import json

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
    primes = get_cached_primes()
    print(f'primes = {primes}')
    not_primes = get_not_primes(primes, n)

    if len(primes) > 0 and n < primes[-1]:
        return [prime for prime in primes if prime <= n]

    if len(primes) == 0:
        start_n = 2
    else:
        start_n = primes[-1] + 1

    for num in range(start_n, n + 1):
        if num % 1000 == 0:
            print(f'{num} of {n} complete')
            save_primes_to_cache(primes)
        if num not in not_primes:
            primes.append(num)
            new_not_prime = num * num
            while new_not_prime <= n:
                not_primes.append(new_not_prime)
                new_not_prime += num
    save_primes_to_cache(primes)
    return primes


def get_not_primes(primes: list, n: int):
    not_primes = []
    for prime in primes:
        new_not_prime = prime * prime
        while new_not_prime <= n:
            not_primes.append(new_not_prime)
            new_not_prime += prime
    return not_primes

def save_primes_to_cache(primes: list):
    cached_primes = get_cached_primes()
    # print(f'cached primes = {cached_primes}\nlen = {len(cached_primes)}')
    new_primes = [prime for prime in primes if prime not in cached_primes]
    # print(f' new primes = {new_primes}\nlen = {len(new_primes)}')
    if len(new_primes) > 0:
        cached_primes = cached_primes + new_primes
        # print(f'cached primes = {cached_primes}\nlen = {len(cached_primes)}')
        with open('cached_primes.json', 'w') as cache_file:
            json.dump(cached_primes, cache_file)
    return


def get_cached_primes():
    try:
        with open('cached_primes.json', 'r') as cache_file:
            primes = json.load(cache_file)
        return primes
    except FileNotFoundError:
        return []

