"""
Write a program that for an arbitrary positive integer N (read from the keyboard) prints the number of zeros, odd digits, and even digits.
"""

import sys

number = int(input('Provide a positive integer: '))
if number < 0:
    print('Input is not postivie integer')
    sys.exit(1)

odd = 0
even = 0
zeros = 0

while number != 0:
    if number % 10 == 0:
        zeros += 1
    elif number % 10 % 2 == 0:
        even += 1
    else:
        odd += 1
    number = int(number / 10)


print('Zeros:', zeros, ' Odd:', odd, ' Even:', even)