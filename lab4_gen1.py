import math

n = int(input())
def my_generator1(n):
    value = 0
    while value < n:
        yield value * value
        value += 1
for value in my_generator1(n):
    print(value, end = " ")

print()

def my_generator1(n):
    value = 0
    while value <= n:
        yield value * value
        value += 1
for value in my_generator1(n):
    print(value, end = " ")