'''
Problem 42:

The nth tern of the sequence of triangle numbers is given by, tn = 1/2n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its aplphabetical position and adding these values we form a
word value.  For example, the word SKY is 19 + 11 + 25 = 55 = t10.  If the word value is a triangle number then we shall
call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
'''


# ------------ import data
import csv

with open('Problem_42_words.txt', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)[0]

# ------------- find longest word in data and compute enough traingle numbers to cover that range

longest_word = data[0]

for word in data:
    if len(word) > len(longest_word):
        longest_word = word

max_tri_num = len(longest_word) * 26

triangle_nums = []
n = 1
triangle_nums = [int(1/2*n*(n+1))]

while max(triangle_nums) < max_tri_num:
    n += 1
    triangle_nums += [int(1/2*n*(n+1))]

# ------------- calculate the numeric value for each word in the file and add to list if it is triangular

def letter_to_num(let):
    return ord(let.lower()) - 96

triangle_words = 0

for word in data:
    numeric_value = 0
    for letter in word:
        numeric_value += letter_to_num(letter)
    
    if numeric_value in triangle_nums:
        triangle_words += 1

print(triangle_words)
