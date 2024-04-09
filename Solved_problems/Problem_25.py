import math

A = int(1)
B = int(1)
C = A + B
index = 2
digits = 1

# print(f'index: {index}, {A} + {B} = {C}')

def count_digits(n):
	return int(math.log10(n)) + 1

while digits < 1000:
	C = A + B
	A = B 
	B = C
	index += 1
	digits = count_digits(C)

print(f'index: {index}, {A} + {B} = {C}, digits = {digits}')

