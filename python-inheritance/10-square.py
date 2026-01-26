#!/usr/bin/python3
"""Module containing Square class that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a square with size

        Args:
            size (int): The size of the square (both width and height)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
