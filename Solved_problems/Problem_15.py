"""
Problem 15: Lattice Paths
----------------------------------


Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

see link for picture: https://projecteuler.net/problem=15

How many such routes are there through a 20×20 grid?
"""


def solution():
    n = 20
    current_row = [0]
    for i in range(n + 1):
        current_row.append(1)

    for i in range(n):
        next_row = [1]
        for y in range(1, n + 1):
            next_row.append(next_row[y-1]+current_row[y])
        current_row = next_row

    print('solution', current_row[-1])
    return

# SEE EXCEL SHEET