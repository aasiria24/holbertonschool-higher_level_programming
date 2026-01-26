#!/usr/bin/env python3
"""Task 01: Duck Typing with Abstract Base Classes"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape"""

    def __init__(self, radius):
        """Initialize a circle with given radius"""
        self.radius = radius

    def area(self):
        """Calculate area of circle: πr²"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate perimeter (circumference) of circle: 2πr"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""

    def __init__(self, width, height):
        """Initialize a rectangle with given width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle: width × height"""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of rectangle: 2(width + height)"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of any shape object.
    Uses duck typing - expects object to have area() and perimeter() methods.
    """
    try:
        area = shape.area()
        perimeter = shape.perimeter()
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
    except AttributeError as e:
        print(f"Error: The object doesn't have required methods. {e}")
