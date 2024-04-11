"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations

ini_str = "0123456789"

permutations = [''.join(p) for p in permutations(ini_str)]

i = 0

while i < 999999:

	print(i+1, permutations[i])
	i += 1

print(f'The one millionth permutation is: {permutations[i]}')
