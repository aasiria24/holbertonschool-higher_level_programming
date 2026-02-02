#!/usr/bin/python3

def read_file(filename=""):
    """
    Read a text file (UFT-8) and prints its content to stdout.

    Args:
    filename (str): The name/path of the file to read.

    Returns:
    None
    """
    with open(filename, 'r', encoding='uft-8') as file:
        for line in file:
            print(line, end='')
