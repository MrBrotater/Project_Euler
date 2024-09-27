# did not bother making this code fancy because the pattern becomes clear when visualized in the problem

n = 1
offset = 2
sum = n

max_n = 1001*1001

while n < max_n:
    for corner in range(0, 4):
        n += offset
        print(n)
        sum += n
    offset += 2

print(sum)
