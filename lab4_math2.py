import math

h = int(input())
x = int(input())
x1 = int(input())
def myfunction1(h, x, x1):
    area = h * (x + x1) / 2
    return area
print("Height: ", h)
print("Base, first value: ", x)
print("Base, second value: ", x1)
print("Expected Output: ", myfunction1(h, x, x1))