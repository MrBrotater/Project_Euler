"""
Problem 3: Largest Prime Factor
----------------------------------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from Reuseable_Functions import is_x_a_multiple_of_y


def is_prime(n):
    if n <= 1:
        return False
    else:
        checked = []
        for i in range(2, n):
            print('----------------------------------------------------------------')
            print(f'checking if {n} is a multiple of {i}')
            if i in checked:
                print(f'{i} is a multiple of a previously checked number')
                pass
            elif n % i == 0:
                print(f'{n} is not prime because it is a multiple of {i}')
                return False
            else:
                checked.append(i)
                for x in range(i, n):
                    print(f'x: {x}')
                    if is_x_a_multiple_of_y(x, i):
                        print(f'{x} is a multiple of {i}, added to checked list')
                        checked.append(x)
        print(f'{n} is a prime number')
        return True


def solution():
    primes = []
    for i in range(100):
        if is_prime(i):
            primes.append(i)
    print(primes)
    return
