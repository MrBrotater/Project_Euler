"""
If p is the perimeter of a right angle triangle with integral length sides, {a, b, c} , there are exactly three solutions for p = 120

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1,000 is the number of solutions maximised?
"""

max_perimeter = 1000


# Euclid's formula for pythagorean triples per wikipedia
def pythagorean_triple(m, n):
	a = m**2 - n**2
	if a < 1:
		return [False]
	if a >1000:
		return [False]
	b = 2*m*n
	if b > 1000:
		return [False]
	c = m**2 + n**2
	p = a + b + c
	if p > 1000:
		return [False]
	return [True, (a, b, c), p]


# Generate list of pythagorean triples
pythagorean_triples = []

for m in range(1, 33):
		for n in range(1, 33):
			if m + n < 1000:
				result = pythagorean_triple(m, n)
				if result[0]:
					pythagorean_triples.append(result[1])


#Initial list is missing some non-primitive triangles, so calculate the remaining ones and add to the list
for triple in pythagorean_triples:
	a = triple[0]
	b = triple[1]
	c = triple[2]
	p = a + b + c
	multiple = 2
	run = True
	while run:
		new_a = a*multiple
		new_b = b*multiple
		new_c = c*multiple
		p = new_a + new_b + new_c
		multiple += 1
		if p <= 1000:
			new_triple = (new_a, new_b, new_c)
			if new_triple not in pythagorean_triples:
				pythagorean_triples.append(new_triple)
		else:
			run = False

#Remove duplicates / not sure if this is necessary
for triple in pythagorean_triples:
	a = triple[0]
	b = triple[1]
	b = triple[2]
	possible_duplicate = (b, a, c)
	if possible_duplicate in pythagorean_triples:
		pythagorean_triples.remove(possible_duplicate)


#test that values given in the problem are detected
test_vals = [(20,48,52), (24,45,51), (30,40,50)]

for val in test_vals:
	a = val[0]
	b = val[1]
	c = val[2]
	if (a,b,c) in pythagorean_triples:
		print("found",val)
	elif(b,a,c) in pythagorean_triples:
		print("found", val)
	else:
		print("not found",val)

# calculate the number of unique solutions for each perimeter value
perimeters = dict()

for triple in pythagorean_triples:
	a = triple[0]
	b = triple[1]
	c = triple[2]
	p = a + b + c
	if p not in perimeters:
		perimeters[p] = [triple]
	else:
		perimeters[p].append(triple)

p_with_max_solutions = int()
max_solutions = int()

for p in perimeters:
	solutions = perimeters[p]
	no_solutions = len(solutions)
	if no_solutions > max_solutions:
		p_with_max_solutions = p
		max_solutions = no_solutions

print(f'There are {max_solutions} integer right triangles with a perimeter of {p_with_max_solutions}: {perimeters[p_with_max_solutions]}')
