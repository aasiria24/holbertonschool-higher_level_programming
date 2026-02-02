#!/usr/bin/python3
"""
Module for Student class with serialization and deserialization.
"""


class Student:
    """
    Class that defines a student with serialization capabilities.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings representing attribute names to retrieve.

        Returns:
            dict: Dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list):
            result = {}
            for key in attrs:
                if isinstance(key, str) and hasattr(self, key):
                    result[key] = getattr(self, key)
            return result

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a dictionary.

        Args:
            json (dict): A dictionary where keys are attribute names and values are the new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
