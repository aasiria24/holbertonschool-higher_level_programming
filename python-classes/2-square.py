#!/usr/bin/python3
"""
This module defines a Square class used to represent a square.
The class validates the size value when a new instance is created.
"""


class Square:
    """
    This class represents a square shape.

    It uses a private instance attribute to store the size of the square
    and ensures that the size is always a valid non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        The size must be an integer greater than or equal to zero.
        If the value provided is invalid, an exception is raised.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
