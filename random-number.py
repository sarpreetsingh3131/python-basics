"""
Write a program generating and printing a random telephone number of the form 0XXX-ZYYYYY. The area code consists of a zero followed by three digits (X). The local number can not start with a zero (Z), all other digits (Y) are random.
"""

import random

print('0' + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + '-'
        + str(random.randint(1, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) 
        + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    )