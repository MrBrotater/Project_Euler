"""
Problem 67: Maximum Path Sum II
----------------------------------
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to
solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every
second it would take over twenty billion years to check them all. There is an efficient algorithm to
solve it. ;o)
"""

triangle = triangle.split("\n")
triangle_array = []
for row in triangle:
    row_list = [int(i) for i in row.split(" ")]
    triangle_array.append(row_list)


def solution():
    data = triangle_array

    for y in range(len(data)):  # rows = y
        if y == 0:
            max_sums = [data[y][0]]
        else:
            new_max_sums = []
            for x in range(len(data[y])):  # columns = x
                if x == 0:
                    new_sum = max_sums[x] + data[y][x]
                    new_max_sums.append(new_sum)
                elif x > len(max_sums) - 1:
                    new_sum = max_sums[x-1] + data[y][x]
                    new_max_sums.append(new_sum)
                else:
                    new_sum_1 = max_sums[x] + data[y][x]
                    new_sum_2 = max_sums[x - 1] + data[y][x]
                    new_sum = max([new_sum_1, new_sum_2])
                    new_max_sums.append(new_sum)
            max_sums = new_max_sums
    print(max(max_sums))

    return
