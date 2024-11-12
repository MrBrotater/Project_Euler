'''
Problem 41:

We shall say that an n-digit number is pandigital if it makes use of all the digits
1 to n exactly once.  For example, 2143 is 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

'''
Analysis:
Rather than starting with a prime sieve up to 987,654,321 I thought it may be faster
to find permutations of digits and then check primeness starting from the high end
then counting backwards.  I originally thought that n = 9 would give the highest
pandigital prime but when no answer was found continued down to 8 and 7 before finding
a valid prime.
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
 
def is_prime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

s = '123456789'

solution = False

while not solution:
    perms = find_permutations(s)

    for perm in list(reversed(perms)):
        if is_prime(int(perm)):
            print(perm)
            solution = True
            break
    s = s[:-1]


