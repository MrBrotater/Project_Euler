'''
Problem 33:

The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
is correct, is obtained by cancelling the 9s.

We shall consider fractions like 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

'''

curious_pairs = []

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):

            num_1 = a*10 + b
            num_2 = b*10 + c

            if num_1 < num_2:

                if num_1 / num_2 == a / c:
                    curious_pairs += [(num_1, num_2)]

numerator = 1
denominator = 1

for pair in curious_pairs:
    numerator *= pair[0]
    denominator *= pair[1]

print(denominator/numerator)
    
