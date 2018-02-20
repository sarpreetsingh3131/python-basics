"""
Write a program which asks the user to provide a three digit number. The program should then compute the sum of the three digits.
"""

number = int(input('Provide a three digit number: '))
total = int(number % 10)
number /= 10
total += int(number % 10)
total += int(number / 10) 

print('Sum of digits:', total)