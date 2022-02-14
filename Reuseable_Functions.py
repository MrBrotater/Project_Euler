def is_x_a_multiple_of_y(x: int, y: int) -> bool:
    """ returns True if x is a multiple of y, else False """
    if x % y == 0:
        return True
    else:
        return False


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
