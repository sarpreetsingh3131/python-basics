"""
Write a program which computes the BMI (Body Mass Index) for a person. The program will read length and weight from the keyboard and then present the result as output. The BMI is computed as weight/(length)^2, where the length is given in meters and the weight in kilograms.
"""

import math

length = float(input('Give your length in meters: '))
weight = float(input('Give your weight in kilograms: '))

print('Your BMI is:', math.ceil(weight / math.pow(length, 2)))