"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def getArea(self):
        return (f"Area: {self.__length * self.__width}")

    def getPeraimeter(self):
        return (f"Parameter: {2 * (self.__length + self.__width)}")

    def isSquare(self):
        return (f"IsSquare: {self.__width == self.__length}")

ractangle1 = Rectangle(7, 4)
ractangle2 = Rectangle(5, 5)

print(ractangle1.getArea())
print(ractangle1.getPeraimeter())
print(ractangle1.isSquare())

print(ractangle2.isSquare())
    