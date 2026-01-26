#!/usr/bin/python3
"""Module containing a function to check object inheritance"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a specified class

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj is an instance of a_class or its subclasses, False otherwise
    """
    return isinstance(obj, a_class)
