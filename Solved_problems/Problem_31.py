"""
In the United Kingdom the currency is made up of pound(E) and pence(p).  There are eight coins in circulation:

	1p, 2p, 5p, 10p, 20p, 50p, 1E, and 2E

It is possible to make 2E in the following way:

	1x1E + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can 2E be made using any number of coins?
"""

target = 200

a = 0 # number of 200p = max = 1
b = 0 # number of 100p - max = 2
c = 0 # number of 50p - max = 4
d = 0 # number of 20p - max = 10
e = 0 # number of 10p - max = 20
f = 0 # number of 5p - max = 40
g = 0 # number of 2p - max = 100
h = 0 # number of 1p - max = 200

cases = []

for a in range(2):
	for b in range(3):
		for c in range(5):
			for d in range(11):
				for e in range(21):
					for f in range(41):
						for g in range(101):
							subtotal = a*200 + b*100 + c*50 + d*20 + e*10 + f*5 + g*2
							if subtotal <= target:
								h = target - subtotal
							else:
								h = 0
							total = subtotal + h
							if total == target:
								cases.append((a,b,c,d,e,f,g,h))

print(f'There are {len(cases)} ways to make 200p with the given coins')
