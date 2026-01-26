#!/usr/bin/python3
"""Module containing function to add attributes to objects"""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible

    Args:
        obj: The object to add the attribute to
        attr_name (str): The name of the attribute
        attr_value: The value of the attribute

    Raises:
        TypeError: If the object can't have new attributes
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
