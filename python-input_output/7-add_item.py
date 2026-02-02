#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"


def main():
    """
    Main function to load existing list, add new arguments,
    and save back to file.
    """
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
