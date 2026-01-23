# Python Learning Projects

This repository contains a collection of Python projects for learning fundamental to advanced Python programming concepts, as part of the Holberton School curriculum.

## 📚 Projects Overview

### 1. **Python - Hello, World**
**Fundamental Python Concepts**
- Using the Python interpreter
- Printing text and variables using `print`
- Working with strings, indexing, and slicing
- Following Python coding style (PEP 8)
- Using pycodestyle for code validation

**Key Files:**
- `2-print.py` - Print a string
- `3-print_number.py` - Print integer with string
- `4-print_float.py` - Print float with precision
- `5-print_string.py` - String repetition and slicing
- `6-concat.py` - String concatenation
- `7-edges.py` - String slicing (first, last, middle)
- `8-concat_edges.py` - String extraction and concatenation
- `9-easter_egg.py` - The Zen of Python

---

### 2. **Python - Data Structures: Lists, Tuples**
**Working with Lists and Tuples**
- Basic sequence operations
- List manipulation and common patterns
- Tuple operations and immutability

**Key Files:**
- `0-print_list_integer.py` - Print all integers of a list (one per line)
- `1-element_at.py` - Safely retrieve element from list
- `2-replace_in_list.py` - Replace element at specific position
- `3-print_reversed_list_integer.py` - Print list in reverse order
- `4-new_in_list.py` - Replace element in new copy (original unchanged)
- `5-no_c.py` - Remove all 'c' and 'C' characters from string
- `6-print_matrix_integer.py` - Print matrix with required formatting
- `7-add_tuple.py` - Add two tuples (0 for missing values)
- `8-multiple_returns.py` - Return tuple with string length and first character
- `9-max_integer.py` - Find biggest integer in list
- `10-divisible_by_2.py` - Check divisibility by 2 for each element
- `11-delete_at.py` - Delete item at specific position
- `12-switch.py` - Switch values of two variables

---

### 3. **Python - More Data Structures: Set, Dictionary**
**Advanced Data Structures**
- Set operations and manipulations
- Dictionary creation and manipulation
- Common data manipulation patterns

**Key Files:**
- `0-square_matrix_simple.py` - Square each value in matrix
- `1-search_replace.py` - Replace all occurrences in list
- `2-uniq_add.py` - Add all unique integers
- `3-common_elements.py` - Find common elements between sets
- `4-only_diff_elements.py` - Symmetric difference of sets
- `5-number_keys.py` - Count keys in dictionary
- `6-print_sorted_dictionary.py` - Print dictionary sorted by keys
- `7-update_dictionary.py` - Replace or add key/value pair
- `8-simple_delete.py` - Delete key from dictionary
- `9-multiply_by_2.py` - Multiply all dictionary values by 2
- `10-best_score.py` - Find key with biggest value
- `11-multiply_list_map.py` - Multiply list values using `map`
- `12-roman_to_int.py` - Convert Roman numerals to integers

**Advanced Tasks:**
- `100-weight_average.py` - Compute weighted average
- `101-square_matrix_map.py` - Square matrix using `map` only
- `102-complex_delete.py` - Delete keys with specific value

---

### 4. **Python - Exceptions**
**Error and Exception Handling**
- Using `try`, `except`, and `finally`
- Handling type errors and division errors
- Working safely with lists
- Raising built-in Python exceptions
- Writing defensive and robust Python code

**Key Files:**
- `0-safe_print_list.py` - Print x elements of any list safely
- `1-safe_print_integer.py` - Print integer with validation
- `2-safe_print_list_integers.py` - Print only integers from list
- `3-safe_print_division.py` - Divide integers with safe printing
- `4-list_division.py` - Divide elements of two lists
- `5-raise_exception.py` - Raise TypeError exception
- `6-raise_exception_msg.py` - Raise NameError with custom message

---

### 5. **Python - Test Driven Development**
**Test-Driven Development (TDD)**
- Writing functions following TDD principles
- Strict input validation and clear error messages
- Writing documentation and tests before implementation
- Using `doctest` and `unittest` frameworks

**Key Files:**
- `0-add_integer.py` - Add two integers with validation
- `1-matrix_divided.py` - Divide all elements of matrix
- `2-say_my_name.py` - Print formatted name
- `3-print_square.py` - Print square using # character
- `4-text_indentation.py` - Print text with new lines after ., ?, :
- `5-max_integer_test.py` - Unittests for max_integer function
- `6-matrix_mul.py` - Multiply two matrices with validation
- `7-lazy_matrix_mul.py` - Matrix multiplication using NumPy

**Testing Approach:**
- Write documentation (module + function) and tests first
- Focus on edge cases and defensive programming
- Use both doctest and unittest frameworks
- Test file structure: `tests/` directory with `.txt` and `.py` files

---

## 🛠 Technical Requirements

### Python Scripts
- **Allowed editors**: vi, vim, emacs
- **Python Version**: 3.8.5 (Ubuntu 20.04 LTS)
- **First line**: `#!/usr/bin/python3`
- **Code style**: `pycodestyle` (version 2.7.*)
- **File format**: All files end with a new line
- **Executability**: All files must be executable
- **Documentation**: All modules and functions require proper docstrings

### Testing Requirements
- **Test files location**: Inside `tests/` folder
- **Test file formats**: `.txt` for doctest, `.py` for unittest
- **Test execution**: 
  - Doctest: `python3 -m doctest ./tests/*`
  - Unittest: `python3 -m unittest tests.module_test`

## 🚀 Getting Started

### Installation
```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd python-learning-projects

# Make scripts executable
chmod +x *.py

### Running Tests
```bash
# Run doctests
python3 -m doctest ./tests/* -v

# Run unittests
python3 -m unittest discover tests -v

# Check code style
pycodestyle *.py
```
---

Project Structure

```text
python-learning-projects/
├── README.md                    # Main documentation
├── python-hello_world/          # Basic Python concepts
├── python-data_structures/      # Lists and tuples
├── python-more_data_structures/ # Sets and dictionaries
├── python-exceptions/           # Error handling
├── python-test_driven_development/ # TDD practices
└── tests/                       # Test files
```
## 📖 Learning Objectives
By completing these projects, you will be able to:

### General Skills
- Write clean, maintainable Python code following PEP 8

- Implement Test-Driven Development practices

- Handle errors and exceptions gracefully

- Work with Python's built-in data structures effectively

- Write comprehensive documentation and tests

### Technical Skills
- String manipulation and formatting

- List, tuple, set, and dictionary operations

- Matrix operations and manipulations

- File I/O operations

- Command-line argument parsing

- Modular programming and code organization

## 👥 Authors
**Amaal Asiri** - Holberton School Student
---

## 📄 License
This project is open source and available for educational purposes as part of the Holberton School curriculum.
