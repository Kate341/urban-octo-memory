class Shape():
    def __init__(shape):
        shape.length = 0
    def area(shape):
        print(shape.length**2)

class Square(Shape):
    def __init__(square):
        square.length = int(input())
    def area(square):
        print(square.length**2)
class Rectangle(Shape):
    def __init__(rectangle):
        rectangle.width = 0
    def get(rectangle):
        rectangle.length = int(input())
        rectangle.width = int(input())
    def area(rectangle):
        print(rectangle.length*rectangle.width)

s1 = Square()
s1.area()
s2 = Rectangle()
s2.get()
s2.area()
print(s2.length)