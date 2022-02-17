"""
Problem 22: Names Scores
----------------------------------
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
over five-thousand first names, begin by sorting it into alphabetical order. Then working
out the alphabetical value for each name, multiply this value by its alphabetical position
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth
    3 + 15 + 12 + 9 + 14 = 53
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def alphab_value(n: str) -> int:
    return ord(n) - 64


def solution():
    with open('Working_on/Problem_22_names.txt', 'r') as f:
        names = f.read()
    names = names.replace('"', '')
    names = names.split(',')
    names.sort()

    i = 1
    total_score = 0

    for name in names:
        name_sum = 0
        for ltr in name:
            name_sum += alphab_value(ltr)
        total_score += i * name_sum
        i += 1
    print(total_score)
    return

# first attempt = 850081394 (INCORRECT)
