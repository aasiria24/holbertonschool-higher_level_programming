#!/usr/bin/python3
"""Defines a Square class with a validated size property and area method."""


class Square:
    """Represents a square with a private validated size."""

    def __init__(self, size=0):
        """Initialize a square with optional size."""
        self.size = size

        @property
        def size(self):
        """Getter method to retrieve th size of the square."""
            return self.__size

            @size.setter
            def size(self, value):
            """Setter method to set the size of the square."""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def area(self):
                """Calcualte and return the current area of the square."""
                return self.__size ** self.__size
