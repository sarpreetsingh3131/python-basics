"""
Write a program which reads a number of seconds (an integer) and then prints the same amount of time given in hours, minutes and seconds.
"""

seconds = int(input('Give a number of seconds: '))
hours = int(seconds / 3600)
seconds -= int(hours * 3600)
minutes = int(seconds / 60)
seconds -= int(minutes * 60)

print('This corresponds to:', hours , 'hours,', minutes, 'minutes and', seconds, 'seconds.')