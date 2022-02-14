import math


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


def is_prime(n, already_checked=None):  # todo this needs major work, should do prime factorial method
    """ return True if number n is prime """
    if already_checked is None:
        already_checked = []
    max_n = int(math.sqrt(n))
    if n <= 1:
        return False
    else:
        checked = already_checked
        for i in range(2, max_n):
            if i in already_checked:
                pass
            elif n % i == 0:
                return False
            else:
                for x in range(i, max_n):
                    if is_x_a_multiple_of_y(x, i):
                        checked.append(x)
        return True, checked
