### Python OOP Tasks
A collection of tasks and exercises to practice Object-Oriented Programming concepts in Python, including file handling, serialization, and mathematical algorithms.

## Tasks
**Task 0: Read File**
- File: `0-read_file.py`
- A function that reads a text file (UTF-8) and prints it to stdout.

**Task 1: Write to File**
- File: `1-write_file.py`
- A function that writes a string to a text file (UTF-8) and returns the number of characters written.

**Task 2: Append to File**
- File: `2-append_write.py`
- A function that appends a string to the end of a text file (UTF-8) and returns the number of characters added.

**Task 3: Convert to JSON**
- File: `3-to_json_string.py`
- A function that returns the JSON representation of an object (string).

**Task 4: Convert from JSON**
- File: `4-from_json_string.py`
- A function that returns a Python object represented by a JSON string.

**Task 5: Save Object to JSON File**
- File: `5-save_to_json_file.py`
- A function that writes an object to a text file using JSON representation.

**Task 6: Load Object from JSON File**
- File: `6-load_from_json_file.py`
- A function that creates an object from a JSON file.

**Task 7: Load, Add, Save**
- File: `7-add_item.py`
- A script that adds all command-line arguments to a Python list and saves them to a JSON file.

**Task 8: Convert Class to JSON**
- File: `8-class_to_json.py`
- A function that returns a dictionary description with simple data structure for JSON serialization of an object.

**Task 9: Student Class**
- File: `9-student.py`
- A Student class that represents a student with a method to convert to JSON.

**Task 10: Student Class with Filter**
- File: `10-student.py`
- An enhanced Student class with attribute filtering capability for JSON conversion.

**Task 11: Load Student from JSON**
- File: `11-student.py`
- A Student class with methods for serialization and deserialization from/to JSON.

**Task 12: Pascal's Triangle**
- File: `12-pascal_triangle.py`
- A function that returns Pascal's triangle for a given integer.

## How to Run
- Make sure Python 3 is installed
- Run the main files for each task:

```bash 
# Example for Task 0
python3 0-main.py

# Example for Task 12
python3 12-main.py
```
## Concepts Covered:

- File handling using with statement
- JSON serialization and deserialization
- Object-Oriented Programming (OOP) and classes
- Exception handling
- Mathematical data structures

## Requirements:
- Python 3.x
- No external libraries required

## License
This project is for educational and learning purposes.

## Example Usage
```python
# Task 0 example
from 0_read_file import read_file
read_file("example.txt")

# Task 8 example
from 8_class_to_json import class_to_json
obj = MyClass("John", 25)
print(class_to_json(obj))

# Task 12 example
from 12_pascal_triangle import pascal_triangle
triangle = pascal_triangle(5)
for row in triangle:
    print(row)
```

## Authors:
**Amaal Asiri**, Holberton School.
