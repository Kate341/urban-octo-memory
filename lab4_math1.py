import math

degree = int(input())
x = 180 / degree
radian = round(math.pi, 6) / x
radian = round(radian, 6)

print("Input degree: ", degree)
print("Output radian: ", radian)
