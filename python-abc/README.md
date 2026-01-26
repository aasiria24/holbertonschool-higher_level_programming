# Python OOP Exercises - Advanced Concepts

## 📚 Overview
A comprehensive collection of Python exercises focusing on advanced Object-Oriented Programming (OOP) concepts including Abstract Classes, Interfaces, Duck Typing, Subclassing, Multiple Inheritance, and Mixins.

## 🎯 Learning Objectives
- **Abstract Classes**: Understand and apply abstract classes to define common interfaces
- **Duck Typing**: Grasp the concept of interfaces and duck typing for flexible polymorphism
- **Subclassing**: Extend standard base classes like lists, dictionaries, and iterators
- **Method Overriding**: Enhance or alter base class methods
- **Multiple Inheritance**: Implement complex relationships between classes
- **Mixins**: Compose behavior across unrelated classes

## 📁 Project Structure
python-abc/
│
├── task_00_abc.py # Abstract Base Classes - Animal hierarchy
├── task_01_duck_typing.py # Duck Typing - Shapes with abstract classes
├── task_02_verboselist.py # Subclassing - Custom list with notifications
├── task_03_countediterator.py # Iterator subclassing with counter
├── task_04_flyingfish.py # Multiple Inheritance - FlyingFish
├── task_05_dragon.py # Mixins - Dragon with multiple abilities
│
└── README.md # This file

## 🚀 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/python-abc.git

# Navigate to the directory
cd python-abc

# Ensure Python 3 is installed
python3 --version
```
## 🔍 Key Concepts Demonstrated
Abstract Base Classes (ABC)
- Use ABC metaclass and @abstractmethod decorator

- Prevent instantiation of incomplete classes

- Define interfaces for derived classes

Duck Typing
- "If it walks like a duck and talks like a duck, it's a duck!"

- Focus on behavior rather than type

- Enables polymorphism without inheritance

Subclassing Built-in Types
- Extend functionality of Python's core types

- Override methods while preserving original behavior

- Create specialized data structures

Multiple Inheritance
- Inherit from multiple parent classes

- Understand Method Resolution Order (MRO)

- Resolve method conflicts

Mixins
- Small, focused classes adding specific behavior

- Composition over inheritance

- Reusable across unrelated classes

## 🏆 Best Practices Learned
- Favor Composition over Inheritance: Use mixins for reusable behavior

- Program to Interfaces: Use abstract classes to define contracts

- Keep Classes Small: Single Responsibility Principle

- Use Duck Typing Wisely: Flexible but requires good documentation

- Understand MRO: Crucial for multiple inheritance scenarios

- Override Methods Properly: Use super() to maintain parent behavior

## 🤝 Contributing
- Fork the repository

- Create a feature branch (git checkout -b feature/improvement)

- Commit changes (git commit -am 'Add new feature')

- Push to branch (git push origin feature/improvement)

- Create Pull Request

  ## 👥 Authors
  **Amaal Asiri** As part of Holberton School Project
