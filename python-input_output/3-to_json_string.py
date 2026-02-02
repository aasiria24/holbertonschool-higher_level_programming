#!/usr/bin/python3
"""
Module to returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Write a function that returns the JSON representation
    of an object (string).

    Args:
    my_obj: The object to convert to JSON.

    Returns:
    str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
