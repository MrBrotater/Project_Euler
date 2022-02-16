"""
Problem 17: Number Letter Counts
----------------------------------
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
"and" when writing out numbers is in compliance with British usage.
"""


def number_to_word(n):
    one_to_nine = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    ten_to_nineteen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
                       'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hundreds = [x + 'hundred' for x in one_to_nine]

    if n < 10:
        num_word = one_to_nine[n - 1]
    elif 10 <= n <= 19:
        num_word = ten_to_nineteen[n - 10]
    elif n % 10 == 0:
        if n % 100 == 0:
            num_word = hundreds[n // 100 - 1]
        else:
            num_word = tens[n // 10 - 2]
    elif 20 <= n <= 99:
        num_word = tens[n // 10 - 2] + one_to_nine[n % 10 - 1]
    else:
        num_word = hundreds[n // 100 - 1] + 'and' + tens[n % 100 // 10 - 1] + one_to_nine[(n % 100) % 10 - 1]

    return num_word


def solution():
    count = 0
    for n in range(1, 200):
        word = number_to_word(n)
        count += len(word)
        print(word, count)
    print('100', number_to_word(100))
    return
