"""
Write a program which for any given positive integer N (read from the keyboard) computes the largest integer K such that 0+2+4+6+8+...+K < N.
"""

number = int(input('Give a positive integer: '))

count = 0
total = 0

while total < number:
    count += 2
    total += count

print('The largest K such that 0 + 2 + 4 + 6 + ... + K <', number, '=> K =', count - 2)