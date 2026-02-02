#!/usr/bin/python3
"""
Module to create an object from json file.
"""
import json


def load_from_json_file(filename):
    """
    create an object from "JSON file".

    Args:
    filename (str): The name of the JSON file.

    Return:
    object: The Python data structure represented by JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
