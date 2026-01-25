#!/usr/bin/python3
"""Defines a Square class that supports comparisons by area."""

class Square:
    """Represents a square with a private validated size."""

    def __init__(self, size=0):
        """Initialize a new Square with an optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Return True if areas are equal."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if areas are not equal."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this area is less than other's area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this area is less than or equal to other's area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this area is greater than other's area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this area is greater than or equal to other's area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()
