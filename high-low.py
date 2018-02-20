"""
Write a program implementing the game High and Low. The computer chooses a random integer between 1 and 100 and lets the user guess the value. After each guess, the user is given a clue of the type “higher” or “lower”.
"""

import random

print('Guess a number between 1 and 100 in 10 tries')

number = random.randint(1, 100)
count = 1

while count <= 10:
    guess = int(input('Guess ' + str(count) + ': ' ))
    if guess == number:
         print('Correct answer after only', count, 'guess(es) – Excellent!')
         break
    elif count == 10:
        print('You Fail, correct answer is ', number)
        break
    elif guess < number:
        print('Clue: higher')
    else:
        print('Clue: lower')
    count += 1

