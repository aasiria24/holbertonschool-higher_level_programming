Python - Exceptions

This project focuses on handling errors and exceptions in Python using try, except, and finally. The tasks demonstrate how to safely handle unexpected inputs, runtime errors, and explicitly raised exceptions without crashing the program.

Project Overview

In this project, you will practice:

Using try / except / finally

Handling type errors and division errors

Working safely with lists

Raising built-in Python exceptions

Writing defensive and robust Python code

Tasks

Task 0: Safe Print List

Write a function that prints x elements of a list.

Prototype:

def safe_print_list(my_list=[], x=0):

Requirements:

my_list can contain any type

Print all elements on the same line followed by a new line

x can be greater than the length of the list

Return the real number of elements printed

Use try / except

Do not use len()

Do not import any module

Task 1: Safe Print Integer

Write a function that prints an integer using formatting.

Prototype:

def safe_print_integer(value):

Requirements:

value can be any type

Print the integer followed by a new line

Return True if printed correctly, otherwise False

Use try / except

Use "{:d}".format()

Do not use type()

Do not import any module

Task 2: Safe Print List of Integers

Write a function that prints the first x elements of a list, but only integers.

Prototype:

def safe_print_list_integers(my_list=[], x=0):

Requirements:

Skip non-integer values silently

Print all integers on the same line followed by a new line

x represents the number of elements to access

If x is greater than list length, an exception is expected

Return the real number of integers printed

Use try / except

Use "{:d}".format()

Do not use len()

Do not import any module

Task 3: Safe Print Division

Write a function that divides two integers and prints the result.

Prototype:

def safe_print_division(a, b):

Requirements:

Assume a and b are integers

Print the result inside the finally block as:
Inside result: <result>

Return the division result or None

Use try / except / finally

Use "{}".format()

Do not import any module

Task 4: List Division

Write a function that divides elements of two lists element by element.

Prototype:

def list_division(my_list_1, my_list_2, list_length):

Requirements:

Return a new list of length list_length

If division fails, append 0 to the result list

Print error messages based on the error:

wrong type

division by 0

out of range

Use try / except / finally

Do not import any module

Task 5: Raise Exception

Write a function that raises a TypeError exception.

Prototype:

def raise_exception():

Requirements:

Do not import any module

Task 6: Raise Exception with Message

Write a function that raises a NameError exception with a custom message.

Prototype:

def raise_exception_msg(message=""):

Requirements:

Do not import any module

Author

Amaal Asiri

License

This project is open source and available for educational purposes.

