import math

number_of_sides = int(input())
length_of_side = int(input())

area = number_of_sides * pow(length_of_side, 2) / 4 * math.tan(math.pi / number_of_sides)
area = math.ceil(area)

print("Input number of sides: ", number_of_sides)
print("Input the length of a side: ", length_of_side)
print("The area of the polygon is: ", area)