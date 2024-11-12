'''
Problem 43:

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each 
of the digits 0 to 9 in some order, but it also has a rather interesting sub-string
divisibility property.

let d1 be the 1st digit, d2 be the 2nd digit, and so on.  In this way, we note the
following:

    d2*d3*d4 = 406 is divisible by 2
    d3*d4*d5 = 063 is dibisible by 3
    d4*d5*d6 = 635 is divisible by 5
    d5*d6*d7 = 357 is divisible by 7
    d6*d7*d8 = 572 is divisible by 11
    d7*d8*d9 = 728 is divisible by 13
    d8*d9*d10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

def find_permutations(s):  
    # recursive function to compute permutations found online, not original
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i, c in enumerate(s):
            for perm in find_permutations(s[:i] + s[i+1:]):
                perms.append(c + perm)
        return perms

def sub_divisible(n):
    n = str(n)
    tests = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        if int(n[i:i+3]) % tests[i-1] != 0:
            return False
    return True

s = '0123456789'

perms = find_permutations(s)

solution = 0

for perm in perms:
    if perm[0] != '0':  # exclude perms with a leading 0
        if sub_divisible(perm):
            solution += int(perm)

print(solution)
