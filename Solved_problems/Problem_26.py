'''
Problem 26:

A unit fraction contains 1 in the numerator.  The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2 = 0.5
    1/3 = 0.(3)
    1/4 = 0.25
    1/5 = 0.2
    1/6 = 0.1(6)
    1/7 = 0.(142857)
    1/8 = 0.125
    1/9 = 0.(1)
    1/10 = 0.1

Where 0.1(6) means 0.166666666...., and has a 1-digit recurring cycle.  It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

# Part 1: recursively generate decimal digits

def division_step(digits, numerator, denominator):
    digit = numerator * 10 // denominator
    digits += str(digit)
    remainder = numerator * 10 - digit * denominator
    numerator = remainder

    return [digits, numerator, denominator]

def recursive_long_division(numerator, denominator, num_cycles):
    cycle = division_step("", numerator, denominator)

    for x in range(num_cycles):
        cycle = division_step(cycle[0], cycle[1], cycle[2])

    return cycle[0]

numerator = 1
denominator = 7
num_cycles = 20

digits = recursive_long_division(numerator, denominator, num_cycles)


# Part 2: Detect recurring cycles in the generated decimal digits

import re

def find_repeating_cycle(string):
    regex = r"([0-9]{4,})(?=\1+)"    # the {4,} term is necessary or else function faults on repeated digits 
    match = re.search(regex, string)
    
    if match == None:
        return ""

    else:
        simplified = False

        while not simplified:

            if match == None:
                simplified = True

            else:
                next_match = re.search(regex, match.group(1))
                if next_match == None:
                    simplified = True
                    return f"{match.group(1)}"
                match = next_match

        return f"{match.group(1)}"

# Part 3: Attempt to solve problem

d_with_longest_cycle = int()
longest_cycle = ""
dec_length = 2000

for d in range(1,1000):
    decimal_string = recursive_long_division(1, d, dec_length)
    repeating_cycle = find_repeating_cycle(decimal_string)
    if len(repeating_cycle) > len(longest_cycle):
        d_with_longest_cycle = d
        longest_cycle = repeating_cycle

print(d_with_longest_cycle)



