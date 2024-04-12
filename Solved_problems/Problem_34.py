"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

def get_digits(n):  # str method
	return [int(x) for x in str(n)]

factorials = {
	0: 1,
	1: 1,
	2: 2,
	3: 6,
	4: 24,
	5: 120,
	6: 720,
	7: 5040,
	8: 40320,
	9: 362880
}

def sum_factorial_digits(n):
	return sum(factorials[x] for x in get_digits(n))

for n in range(3,41000):  # according to project euler 40585 is the highest value, but I did not figure a way to prove it

	result = sum_factorial_digits(n)
	if n == result:
		print(n)
