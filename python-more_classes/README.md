# Python - More Classes and Objects

This repository contains a series of Python projects focusing on Object-Oriented Programming (OOP) concepts. Each task builds upon the previous one to deepen understanding of classes, objects, and their associated concepts in Python.

## Tasks Overview

### 0. Empty rectangle
**File:** `0-rectangle.py`  
**Description:** An empty class `Rectangle` that defines a rectangle.

### 1. Real definition of a rectangle
**File:** `1-rectangle.py`  
**Description:** A `Rectangle` class with private instance attributes `width` and `height`, including:
- Property getters and setters with validation
- Type checking (must be integers)
- Value checking (must be >= 0)

### 2. Area and Perimeter
**File:** `2-rectangle.py`  
**Description:** Adds methods to calculate:
- `area()`: Returns the rectangle area
- `perimeter()`: Returns the rectangle perimeter (0 if width or height is 0)

### 3. String representation
**File:** `3-rectangle.py`  
**Description:** Implements the `__str__` method to print the rectangle using `#` characters.

### 4. Eval is magic
**File:** `4-rectangle.py`  
**Description:** Implements the `__repr__` method to return a string representation that can recreate a new instance using `eval()`.

### 5. Detect instance deletion
**File:** `5-rectangle.py`  
**Description:** Implements the `__del__` method to print a message when an instance is deleted.

### 6. How many instances
**File:** `6-rectangle.py`  
**Description:** Adds a public class attribute `number_of_instances` that:
- Tracks the number of active instances
- Increments during instantiation
- Decrements during deletion

### 7. Change representation
**File:** `7-rectangle.py`  
**Description:** Adds a public class attribute `print_symbol` that:
- Can be any type
- Used as the symbol for string representation
- Can be modified at instance or class level

### 8. Compare rectangles
**File:** `8-rectangle.py`  
**Description:** Adds a static method `bigger_or_equal()` that:
- Compares two rectangles based on area
- Returns the rectangle with larger or equal area
- Includes type validation

### 9. A square is a rectangle
**File:** `9-rectangle.py`  
**Description:** Adds a class method `square()` that:
- Creates a new rectangle instance
- Width and height are equal to the given size
- Returns a square (special case of rectangle)

### 10. N Queens
**File:** `101-nqueens.py`  
**Description:** A program that solves the N Queens puzzle:
- Places N non-attacking queens on an N×N chessboard
- Uses backtracking algorithm
- Handles command line arguments and validation

## Concepts Covered

- **Classes and Objects:** Defining and instantiating classes
- **Attributes:** Instance vs class attributes, public vs private
- **Properties:** Getters and setters with validation
- **Methods:** Instance methods, static methods, class methods
- **Special Methods:** `__init__`, `__str__`, `__repr__`, `__del__`
- **Encapsulation:** Data abstraction and information hiding
- **Class Attributes:** Shared attributes among all instances
- **Backtracking:** Algorithm design for constraint satisfaction problems

## Requirements

- Python 3.8.5
- Ubuntu 20.04 LTS
- Files must be executable
- Code must follow pycodestyle (version 2.7.*)
- Each file must have proper documentation

## Usage

Each Python file can be executed independently. For example:
```bash
chmod u+x 1-rectangle.py
./1-rectangle.py
