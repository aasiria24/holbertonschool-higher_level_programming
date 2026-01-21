#!/usr/bin/python3
"""
Module: 5-text_indentation

Contains function: text_indentation(text)
Prints a text with a new line after each ., ? and :
"""

def text_indentation(text):
    """Prints text with a new line after each ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)

    while i < length:
        print(text[i], end='')  

        if text[i] in ".?:":
            print()  

            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue

        i += 1

    print() 
