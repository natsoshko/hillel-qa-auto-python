from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side size must be greater than 0")
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return self.__side * 4

    # def __str__(self):
    #     return f"Square({self.side})"

class Rectangle(Figure):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Side size must be greater than 0")
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    # def __str__(self):
    #     return f"Rectangle({self.width}, {self.height})"

class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius size must be greater than 0")
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

    # def __str__(self):
    #     return f"Circle({self.__radius})"


figures = [
        Circle(5),
        Rectangle(4, 6),
        Square(3),
]

for figure in figures:
    print(f"{figure.__class__.__name__}:")
    print(f"  Area: {figure.area():.2f}")
    print(f"  Perimeter: {figure.perimeter():.2f}")
    print()


