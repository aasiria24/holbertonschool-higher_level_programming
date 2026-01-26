# Python Inheritance

This repository contains a series of Python projects focusing on inheritance and object-oriented programming concepts in Python. Each task demonstrates different aspects of inheritance, class relationships, and special methods.

## Tasks Overview

### 0. Lookup
**File:** `0-lookup.py`  
**Description:** A function that returns the list of available attributes and methods of an object using the built-in `dir()` function.

### 1. My list
**File:** `1-my_list.py`, `tests/1-my_list.txt`  
**Description:** A class `MyList` that inherits from the built-in `list` class with an additional method `print_sorted()` that prints the list in ascending order without modifying the original list.

### 2. Exact same object
**File:** `2-is_same_class.py`  
**Description:** A function that checks if an object is exactly an instance of the specified class using `type()` and the `is` operator.

### 3. Same class or inherit from
**File:** `3-is_kind_of_class.py`  
**Description:** A function that checks if an object is an instance of, or inherited from, a specified class using `isinstance()`.

### 4. Only sub class of
**File:** `4-inherits_from.py`  
**Description:** A function that checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class, but not an instance of the class itself.

### 5. Base geometry
**File:** `5-base_geometry.py`  
**Description:** An empty `BaseGeometry` class that serves as a base for geometric shapes.

### 6. Improve geometry
**File:** `6-base_geometry.py`  
**Description:** An enhanced `BaseGeometry` class with an `area()` method that raises an exception.

### 7. Integer validator
**File:** `7-base_geometry.py`, `tests/7-base_geometry.txt`  
**Description:** A `BaseGeometry` class with:
- `area()` method that raises an exception
- `integer_validator()` method that validates integer values

### 8. Rectangle
**File:** `8-rectangle.py`  
**Description:** A `Rectangle` class that inherits from `BaseGeometry` with:
- Private width and height attributes
- Validation using `integer_validator()`
- No getters or setters

### 9. Full rectangle
**File:** `9-rectangle.py`  
**Description:** An enhanced `Rectangle` class that:
- Implements the `area()` method
- Overrides `__str__()` to return `[Rectangle] <width>/<height>`

### 10. Square #1
**File:** `10-square.py`  
**Description:** A `Square` class that inherits from `Rectangle` with:
- Size parameter for both width and height
- Inherits `area()` and `__str__()` from Rectangle

### 11. Square #2
**File:** `11-square.py`  
**Description:** An improved `Square` class that overrides `__str__()` to return `[Square] <size>/<size>` instead of the Rectangle format.

### 12. My integer
**File:** `100-my_int.py`  
**Description:** A `MyInt` class that inherits from `int` but inverts the behavior of the `==` and `!=` operators.

### 13. Can I?
**File:** `101-add_attribute.py`  
**Description:** A function that adds a new attribute to an object if possible, raising a `TypeError` if the object can't accept new attributes.

## Key Concepts Covered

- **Inheritance:** Creating subclasses that inherit from parent classes
- **Type Checking:** Using `type()`, `isinstance()`, and `issubclass()`
- **Special Methods:** Overriding `__str__()`, `__eq__()`, `__ne__()`
- **Attribute Management:** Dynamic attribute addition and validation
- **Method Overriding:** Customizing inherited methods
- **Abstract Methods:** Creating base classes with unimplemented methods
- **Validation:** Input validation in class constructors


## Testing

The project includes doctest files for some tasks. Run tests using:

```bash
# For MyList tests
python3 -m doctest ./tests/1-my_list.txt

# For BaseGeometry tests  
python3 -m doctest ./tests/7-base_geometry.txt
```
## Usage
Each Python file can be executed independently. For example:

```bash
# Make the file executable
chmod u+x 1-my_list.py

# Run the example
./1-my_list.py
```
## Author
**Amaal Asiri** as part of Holberton School Project
