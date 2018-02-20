"""
Write a program that reads an arbitrary string from the keyboard and then prints it backwards.
"""

line = input('Provide a line of text: ')

print('Backwards: ', end='')

for letter in reversed(line): 
    print(letter, end='')

print('')