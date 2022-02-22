"""
Problem 21: Amicable Numbers
----------------------------------
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which
divide evenly into n).  If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are:

    1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
    therefore d(220) = 284.

The proper divisors of 284 are:

    1, 2, 4, 71 and 142;
    so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from Working_on.Reuseable_Functions import proper_divisors_of_n

list_to_check = [i for i in range(1, 10000)]
amicable_nos = []
non_amicable_nos = []


def is_amicable(a):
    b = sum(proper_divisors_of_n(a))
    c = sum(proper_divisors_of_n(b))
    if c == a and a != b:
        return True, [a, b]
    else:
        return False, [a]


def solution():
    for i in list_to_check:
        result, nums = is_amicable(i)
        if result:
            for num in nums:
                amicable_nos.append(num)
                if num in list_to_check:
                    list_to_check.remove(num)
        else:
            non_amicable_nos.append(i)
            list_to_check.remove(i)
    print(amicable_nos)
    print(non_amicable_nos)
    print(sum(amicable_nos))

    return
