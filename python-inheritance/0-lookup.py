#!/usr/bin/python3
"""Module containing a function to look up object attributes and methods"""


def lookup(obj):
    """Return a list of available attributes and methods of an object

    Args:
        obj: Any Python object

    Returns:
        list: List of strings containing attribute and method names
    """
    return dir(obj)
