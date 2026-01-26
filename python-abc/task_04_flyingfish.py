#!/usr/bin/env python3
"""Task 04: Multiple Inheritance with FlyingFish"""


class Fish:
    """Fish class representing aquatic animals"""

    def swim(self):
        """Print swimming behavior of fish"""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat of fish"""
        print("The fish lives in water")


class Bird:
    """Bird class representing avian animals"""

    def fly(self):
        """Print flying behavior of bird"""
        print("The bird is flying")

    def habitat(self):
        """Print habitat of bird"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from both Fish and Bird"""

    def fly(self):
        """Override Bird's fly method for flying fish"""
        print("The flying fish is soaring!")

    def swim(self):
        """Override Fish's swim method for flying fish"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat method to reflect dual nature"""
        print("The flying fish lives both in water and the sky!")
