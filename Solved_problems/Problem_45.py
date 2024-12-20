"""
Problem 45:

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle    T(n) = n(n+1)/2     1, 3, 6, 10, 15, ...
pentagonal  P(n) = n(3n-1)/2    1, 5, 12, 22, 35, ...
hexagonal   H(n) = n(2n-1)      1, 6, 15, 28, 45, ...

It can be verified that T(285) = P(165) = H(143) = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

"""
Thoughts:

It was not immediately obvious but eventually figured out that all hexagonal numbers are triangle numbers, 
therefore the problem can be simplified by calculating hexagonal numbers and then checking if they are
pentagonal.
"""

def pentagon(p):
    return p*(3*p-1)/2

def hexagon(h):
    return h*(2*h-1)

p = 166
h = 144

match_found = False

while not match_found:
    next_hex = hexagon(h)
    while pentagon(p) < next_hex:
        p += 1
    if pentagon(p) == next_hex:
        print(f'P({p}) ==  H({h}) == {next_hex}')
        match_found = True
    h += 1
