"""
Problem 15: Lattice Paths
----------------------------------


Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

see link for picture: https://projecteuler.net/problem=15

How many such routes are there through a 20×20 grid?
"""
from itertools import permutations


def solution():  # this probably works, but is far too slow (ran for > 1 hr)
    n = 20
    init_choices = n * 'E' + n * 'S'
    print(init_choices)
    possible_paths = set(permutations(init_choices))

    print(len(possible_paths))
    return
