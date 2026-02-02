#!/usr/bin/python3
"""
Module for returning the dictionary description for JSON serialization
of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: Dictionary description of the object's attributes.
    """
    return obj.__dict__
