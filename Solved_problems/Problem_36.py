"""
Problem 36:

The decimal number, 585=1001001001(binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def isPalindrome(n):
    return str(n) == str(n)[::-1]

base10Palindromes = []

for n in range(1, 1000000):
    if isPalindrome(n):
        base10Palindromes += [n]


def decToBinary(dec):
    binary = ''
    while dec > 0:
        binary += str(dec - (dec // 2) * 2)
        if dec == 1:
            dec = 0
        else:
            dec = dec //2
    return binary[::-1]

baseBothPalindromes = []

for palindrome in base10Palindromes:
    if isPalindrome(decToBinary(palindrome)):
        baseBothPalindromes += [palindrome]

print(sum(baseBothPalindromes))

