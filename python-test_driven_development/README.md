# Python - Test Driven Development

This project focuses on writing Python functions following **Test Driven Development (TDD)** principles.
Each task emphasizes strict input validation, clear error messages, and adherence to Python best practices.
No external modules are allowed unless explicitly stated.

---

## Task 0: Add two integers

### Description
Write a function that adds two integers.

### Prototype
```python
def add_integer(a, b=98):

Requirements
	•	a and b must be integers or floats
	•	Otherwise, raise:
	•	TypeError: a must be an integer
	•	TypeError: b must be an integer
	•	Floats must be cast to integers before addition
	•	Returns an integer
	•	No module imports allowed

⸻
Task 1: Divide a matrix

Description

Write a function that divides all elements of a matrix.

Prototype
def matrix_divided(matrix, div):
Requirements
	•	matrix must be a list of lists of integers or floats
	•	Otherwise:
TypeError: matrix must be a matrix (list of lists) of integers/floats
	•	Each row must be of the same size
	•	Otherwise:
TypeError: Each row of the matrix must have the same size
	•	div must be an integer or float
	•	Otherwise:
TypeError: div must be a number
	•	div must not be 0
	•	Otherwise:
ZeroDivisionError: division by zero
	•	All results are rounded to 2 decimal places
	•	Returns a new matrix
	•	No module imports allowed

⸻

Task 2: Say my name

Description

Write a function that prints:
My name is <first name> <last name>
Prototype
def say_my_name(first_name, last_name=""):
Requirements
	•	first_name and last_name must be strings
	•	Otherwise:
	•	TypeError: first_name must be a string
	•	TypeError: last_name must be a string
	•	No module imports allowed

⸻

Task 3: Print a square

Description

Write a function that prints a square using the character #.

Prototype
def print_square(size):
Requirements
	•	size must be an integer
	•	Otherwise:
TypeError: size must be an integer
	•	If size < 0:
ValueError: size must be >= 0
	•	If size is a float and < 0:
TypeError: size must be an integer
	•	No module imports allowed

⸻

Task 4: Text indentation

Description

Write a function that prints a text with two new lines after each:
	•	.
	•	?
	•	:

Prototype
def text_indentation(text):
Requirements
	•	text must be a string
	•	Otherwise:
TypeError: text must be a string
	•	No space at the beginning or end of each printed line
	•	No module imports allowed

⸻

Task 5: Max integer - Unittest

Description

Write unittests for the function:
def max_integer(list=[]):
Requirements
	•	Tests must be written using the unittest module
	•	Test file must be inside a tests/ directory
	•	Test file extension: .py
	•	Tests must be executed using:
python3 -m unittest tests.6-max_integer_test
	•	All tests must pass using the provided max_integer function
	•	Edge cases are strongly encouraged

⸻

Task 6 (Advanced): Matrix multiplication

Description

Write a function that multiplies two matrices.

Prototype
def matrix_mul(m_a, m_b):
Validation Order & Errors
	1.	m_a and m_b must be lists
	•	TypeError: m_a must be a list
	•	TypeError: m_b must be a list
	2.	Must be lists of lists
	•	TypeError: m_a must be a list of lists
	•	TypeError: m_b must be a list of lists
	3.	Must not be empty ([] or [[]])
	•	ValueError: m_a can't be empty
	•	ValueError: m_b can't be empty
	4.	Elements must be integers or floats
	•	TypeError: m_a should contain only integers or floats
	•	TypeError: m_b should contain only integers or floats
	5.	Must be rectangular
	•	TypeError: each row of m_a must be of the same size
	•	TypeError: each row of m_b must be of the same size
	6.	Must be multipliable
	•	ValueError: m_a and m_b can't be multiplied

	•	No module imports allowed

⸻

Task 7 (Advanced): Lazy matrix multiplication (NumPy)

Description

Write a function that multiplies two matrices using NumPy.

Prototype
def lazy_matrix_mul(m_a, m_b):
Requirements
	•	Uses the NumPy module
	•	Installation:
pip3 install numpy==1.15.0
	•	Test cases are the same as 100-matrix_mul
	•	Exception types/messages differ
	•	This task is not completed

⸻

Author

Amaal Asiri, Holberton School Student.
Python - Test Driven Development
