"""
Problem 18: Maximum Path Sum I
----------------------------------
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

               75
              95 64
             17 47 82
            18 35 87 10
           20 04 82 47 65
          19 01 23 75 03 34
         88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
       41 41 26 56 83 40 80 70 33
      41 48 72 33 47 32 37 16 94 29
     53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
"""

triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

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
