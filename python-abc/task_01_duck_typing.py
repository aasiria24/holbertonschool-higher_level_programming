#!/usr/bin/env python3
"""
Defines an abstract Shape class and concrete implementations
using duck typing.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        pi = 3.141592653589793
        return pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        pi = 3.141592653589793
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape.
    Uses duck typing (no type checking).
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
