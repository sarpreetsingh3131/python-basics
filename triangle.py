"""
Write a program reading a positive odd integer N from the keyboard, and then prints two triangles. First a right-angled triangle, then an isosceles triangle. The program should end with an error message if the input N is not an odd postive integer.
"""

import sys

number = int(input('Provide a postive odd integer: '))
if number < 0 or number % 2 == 0:
    print('Input is not a postive odd integer')
    sys.exit(1)

print('Right-Angled Triangle:')
for i in range(0, number):
    for j in range(i, number):
        print(' ', end='')
    for k in range(0, i + 1):
        print('*', end='')
    print('')

print('Isosceles Triangle:')
for i in range(1, number + 1, 2):
    spaces = ''
    for j in range(0, int(number - i / 2)):
        spaces += ' '
    stars = ''
    for k in range(0, i):
        stars += '*'
    print(spaces + stars + spaces)
