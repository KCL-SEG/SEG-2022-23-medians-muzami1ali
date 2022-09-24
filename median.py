"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from operator import le



while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
length = len(numbers)
if length%2==0:
    x = (length//2)
    y = x - 1
    z = (numbers[x] + numbers[y]) / 2
else:
    x = (length//2)
    z = numbers[x]
    
print(z)