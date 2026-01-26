#!/usr/bin/python3
"""Module containing MyInt class that inherits from int"""


class MyInt(int):
    """MyInt class that inherits from int with inverted == and != operators"""

    def __eq__(self, other):
        """Override == operator to invert its behavior

        Args:
            other: The value to compare with

        Returns:
            bool: True if not equal, False if equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator to invert its behavior

        Args:
            other: The value to compare with

        Returns:
            bool: True if equal, False if not equal
        """
        return super().__eq__(other)
