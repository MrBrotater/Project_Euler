'''
Problem 29:

Consider all integer combinations of a^b for 2 <= a <= 5 and 2 <= b <= 5:

    2^2 = 4, 2^3 = 8, 2^4 = 16, 2^5 = 32
    3^2 = 9, 3^3 = 27 .....

If they are placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

    4, 8, 9, 16, 25, ....., 3125

Howe many distinct terms are in the sequence generated by a^b for 2 <= a <= 100 and 2 <= b <= 100?
'''

terms = []

for a in range (2, 101):
    for b in range(2, 101):
        terms += [a**b]

print(len(set(terms)))
