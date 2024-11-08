pandigital_products = []

for a in range(1, 100):
    for b in range(1, 5000):
        a_str = str(a)
        b_str = str(b)
        digits = set(a_str + b_str)
        if '0' not in digits:
            if len(digits) == 5:
                c = a * b
                if c <= 9876:
                    c_str = str(c)
                    digits = set(a_str + b_str + c_str)
                    if '0' not in digits:
                        if len(digits) == 9:
                            pandigital_products += [c]
                            print(a, b, c, digits)

print(set(pandigital_products))
solution = sum(set(pandigital_products))

print(solution)
