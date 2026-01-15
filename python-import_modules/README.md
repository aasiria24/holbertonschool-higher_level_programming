# Python - import & modules

This project covers modules and imports in Python programming.

## 📚 Project Overview

This project covers fundamental Python concepts including:
- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## 📁 Project Structure
python-import_modules/
├── README.md # This file
├── 0-add.py # Task 0: Import and add function
├── 1-calculation.py # Task 1: Import calculations module
├── 2-args.py # Task 2: Print number of arguments
├── 3-infinite_add.py # Task 3: Infinite addition
├── 4-hidden_discovery.py # Task 4: Discover hidden names
├── 5-variable_load.py # Task 5: Load variable from module
├── (other task files as needed)
└── (module files as required)
## 🎯 Learning Objectives

By completing this project, you will be able to:

### General
- Understand why Python programming is awesome
- Import functions from another file
- Use imported functions effectively
- Create and organize modules
- Use the built-in function `dir()`
- Prevent code execution when a script is imported
- Use command line arguments in Python programs

### Technical Skills
- Write modular Python code
- Create reusable modules
- Handle script vs module execution
- Process command line arguments
- Explore module namespaces

## ⚙️ Requirements

### General
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 22.04 LTS using python3 (version 3.10.*)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Code should use the `pycodestyle` (version 2.7.*)
- All files must be executable
- The length of files will be tested using `wc`

## 🔧 Setup and Usage

### Running Scripts
```bash
# Make the script executable
chmod +x script_name.py

# Run the script
./script_name.py

# Run with arguments
./script_name.py arg1 arg2 arg3
Creating Modules
python
# mymodule.py
def my_function():
    return "Hello from module"

# main.py
import mymodule
print(mymodule.my_function())
📖 Key Concepts
1. Importing in Python
import module_name

from module_name import function_name

from module_name import *

import module_name as alias

2. Module vs Script
Module: File meant to be imported

Script: File meant to be executed directly

Use if __name__ == "__main__": to control execution

3. Command Line Arguments
Access via sys.argv list

sys.argv[0] is the script name

Arguments start from sys.argv[1]

4. Exploring Modules
Use dir(module_name) to see available names

Use help(module_name) for documentation

🛠️ Common Patterns
Preventing Execution on Import
python
#!/usr/bin/python3
# module.py

def function():
    return "I'm a function"

if __name__ == "__main__":
    # This code only runs when executed directly
    print("Executed as script")
    print(function())
Handling Command Line Arguments
python
#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    print(f"Arguments: {sys.argv[1:]}")
else:
    print("No arguments provided")
📚 Resources
Python Modules Documentation

Python Command Line Arguments

PEP 8 -- Style Guide for Python Code

What is if __name__ == "__main__"?
