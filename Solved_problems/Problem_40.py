"""
An irrational decimal fraction is created by concatenating the positive integers:

	0.12345678910_1_11213141516171819202122.......

It can be seen that the 12th digit of the fractional part is 1 (bounded by underscores).

If d(n) represents the nth digit of the fractional part, find the value of the following expression:

d(1) x d(10) x d(100) x d(1000) x d(10000), x d(100000), x d(1000000)

"""

def get_digits(n):
	return [int(x) for x in str(n)]

digits = [1]
n = 2

while n <= 1000000:
	for digit in get_digits(n):
		digits.append(digit)
	n += 1

solution = digits[1-1]*digits[10-1]*digits[100-1]*digits[1000-1]*digits[10000-1]*digits[100000-1]*digits[1000000-1]

print(solution)
