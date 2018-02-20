"""
Write a program that reads 10 integers from the keyboard and then prints the second largest one. 
"""

secondLargest = 0
largest = 0

print('Provide 10 integers: ', end='')

for i in range(0, 10):
    number = int(input())
    if number > largest:
        secondLargest = largest
        largest = number
    elif number > secondLargest:
        secondLargest = number
    
print('The second largest is:',  secondLargest)