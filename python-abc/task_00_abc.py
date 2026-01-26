#!/usr/bin/env python3
"""Task 00: Abstract Base Classes"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal"""

    def sound(self):
        """Returns the sound of a dog"""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal"""
    
    def sound(self):
        """Returns the sound of a cat"""
        return "Meow"
