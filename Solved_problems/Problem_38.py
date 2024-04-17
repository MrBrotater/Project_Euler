"""
Take the number 192 and multiply it by each of 1, 2, and 3:
	192 x 1 = 192
	192 x 2 = 384
	192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.  We will call 192384576
the concatenated product of 192 and (1,2,3).

The same can be achieved by starting with 9 and multiplying 1, 2, 3, 4, and 5, giving the
pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
product of an integer with 1,2,....,n)where n>1?

"""

def pandigital(n): # return (n, (1, 2, 3, ...), pandigital)
	digits = []
	x = 1
	while (len(digits) < 9):
		new_digits = [digit for digit in str(n*x)]
		for digit in new_digits:
			if digit in digits:
				return (n, None, 0)
			else:
				digits += digit
		x += 1
	if len(digits) > 9:
		return (n, None, 0)
	elif '0' in digits:
		return (n, None, 0)
	elif len(digits) == 9:
		return(n,[i for i in range(1, x)], int(''.join(digits)))

highest_n = 0

for n in range(1, 9999):
	result = pandigital(n)

	if result[2] > 0:
		print(result)
		if result[2] > highest_n:
			highest_n = result[2]

print(highest_n)
