"""
Write a program reading a first name and a last name (given name and family name) as two Strings. The output should consist of the first letter of the first name followed by a dot and a space, followed by the first four letters of the last name.
"""

firtName = input('First name: ')
lastName = input('Last name: ')

print('Short name:', firtName[:1] + '.', lastName[:5])