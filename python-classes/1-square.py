#!/usr/bin/python3
"""
Module: 1-square
This module defines a Square with private size attribute.
"""


class Square:
    """
    A class defines a square.

    Attributes:
    __size (int): The size of the square (private attribute).
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
        size (int): The size of the square.
        """
        self.__size = size
