"""
Write a program which reads two coordinates in the form (x,y) and then computes the distance between the points, using the formula distance = Sqrt( (x1-x2)^2 + (y1-y2)^2 ) Sqrt() means "the square root of" and ^ means "raised to". The answer should be presented with three decimal digits.
"""

import math

x1 = int(input('x1: '))
x2 = int(input('x2: '))

y1 = int(input('y1: '))
y2 = int(input('y2: '))

distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

print('Distance:', format(distance, '.3f'))