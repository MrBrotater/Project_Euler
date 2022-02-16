"""
Problem 14: Longest Collatz Sequence
----------------------------------
The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting
numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def n_even(n):
    return n / 2


def n_odd(n):
    return 3 * n + 1


def next_n(n):
    funcs = {0: n_odd, 1: n_even}
    return funcs[n % 2 == 0](n)


def solution():
    max_n = 1000000
    max_count = 0
    start_num = 0
    for n in range(1, max_n):
        count = 1
        i = n
        while i != 1:
            i = next_n(i)
            count += 1
        if count > max_count:
            max_count = count
            start_num = n
            print(f'current longest sequence = {max_count} with starting num {start_num}')

    print(f'solution = {start_num}, sequence length = {max_count}')
    return

# first attempt = 932068 (INCORRECT) solved in 443.1113469 seconds
# had function calls backwards in next_n function dictionary
# second attempt = 837799 (CORRECT) solved in 53.8575394 seconds
