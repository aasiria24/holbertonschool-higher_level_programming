# Python Serialization Examples

This directory contains multiple Python scripts demonstrating different **serialization and deserialization** techniques using common data formats.

## Contents

### 1. JSON Serialization
**File:** `task_00_basic_serialization.py`

- Serialize a Python dictionary into a JSON file
- Load and deserialize JSON back into a dictionary
- Handles UTF-8 encoding and basic error handling

**Libraries used:**
- `json`
- `os`

---

### 2. Pickling Custom Classes
**File:** `task_01_pickle.py`

- Serialize and deserialize custom Python class objects
- Uses the `pickle` module
- Includes type checking after deserialization

**Libraries used:**
- `pickle`
- `os`

---

### 3. CSV to JSON Conversion
**File:** `task_02_csv.py`

- Convert CSV files into JSON format
- Validate CSV files before conversion
- Supports Unicode characters
- Provides basic conversion statistics

**Libraries used:**
- `csv`
- `json`
- `os`

---

### 4. XML Serialization
**File:** `task_03_xml.py`

- Serialize a Python dictionary into an XML file
- Deserialize XML back into a dictionary

**Libraries used:**
- `xml.etree.ElementTree`

---

## How to Run

Make sure you have **Python 3** installed, then run any script directly:

```bash
python3 filename.py
```
### Project Purpose

## This project is intended for learning and practicing:

- Serialization and deserialization concepts

- File handling in Python

- Error handling

- Working with different data formats (JSON, CSV, XML, Pickle)

## Notes

Some scripts include test code inside
if __name__ == "__main__":

Output files (JSON / XML / Pickle) are created in the same directory.

## Authors:
**Amaal Asiri** Holberton School.
