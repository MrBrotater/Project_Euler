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

# Part 1: recursively generate decimal digits  THIS PART IS WORKING!!!!!!!!!

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


# Part 2: Detect recurring cycles in the generated decimal digits  PLAN TO MAYBE USE A REGEX HERE?????

import re

def find_recurring_cycle(digits):
    str_length = len(digits)
    place = str_length - 1
    repeat_detected = True
    length = 0

    while repeat_detected:
        end_section = digits[place:]
        front_section = digits[:place]
        place -= 1
        print(place, front_section, end_section)
        if end_section not in front_section:
            repeat_detected = False
        if place == 1:
            repeat_detected = False
        length += 1
    print(length, end_section)



full_text = "1111111111"

find_recurring_cycle(full_text)
