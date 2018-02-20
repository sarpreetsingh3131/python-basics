"""
Write a program that reads a string from the keyboard and then prints how many 'a' and 'A' the string contains.
"""

line = input('Provide a line of text: ')
lowercase = 0
uppercase = 0

for letter in line:
    if letter == 'a':
        lowercase += 1
    elif letter == 'A':
        uppercase += 1


print('Number of \'a\':', lowercase, '\nNumber of \'A\':', uppercase)
