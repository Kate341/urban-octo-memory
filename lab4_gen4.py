a = int(input())
b = int(input())

def squares(a, b):
    for value in range(a, b + 1):
        yield value * value
print(", ".join(str(value) for value in squares(a, b)))
#First method

import math
a = int(input())
b = int(input())

def squares(a, b):
    for value in range(a, b + 1):
        yield pow(value, 2)
print(", ".join(str(value) for value in squares(a, b)))
#Second method