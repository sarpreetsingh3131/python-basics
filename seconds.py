"""
Write a program which reads three integers (hours, minutes, seconds) and then computes the corresponding time measured in seconds. For example, 1 hour, 28 minutes and 42 seconds is equal to 5322 seconds.
"""

hours = int(input('Hour: ')) * 3600
mins = int(input('Min: ')) * 60
secs = int(input('Sec: '))

print('Total time measured in seconds:', hours + mins + secs)
