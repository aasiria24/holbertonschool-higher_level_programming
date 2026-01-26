#!/usr/bin/python3
"""
BaseGeometry module for Task 7.
"""


class BaseGeometry:
    """Class with area and integer_validator methods."""

    def area(self):
        """Raises an Exception for unimplemented area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as an integer greater than 0.
        Uses type() instead of isinstance() to strictly exclude booleans.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
