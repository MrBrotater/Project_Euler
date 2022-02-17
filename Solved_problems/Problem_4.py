"""
Problem 4: Largest Palindrome Product
--------------------------------------
A palindromic number reads the same both ways. The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    return True if str(n) == str(n)[::-1] else False


def solution():
    palindromic_numbers = []
    for x in range(100, 999):
        for y in range(100, 999):
            z = x * y
            if is_palindrome(z):
                palindromic_numbers.append(z)
                print(f'{z} is a palindrome')
            print(x, y, z)
    largest_palindrome = max(palindromic_numbers)
    print(largest_palindrome)
    return
