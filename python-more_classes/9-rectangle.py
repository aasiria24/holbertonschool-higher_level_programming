#!/usr/bin/python3
"""Module that defines a Rectangle class with class method for squares"""


class Rectangle:
    """Class that defines a rectangle with width and height attributes"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment counter

    @property
    def width(self):
        """Getter method for the width attribute

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute with validation

        Args:
            value (int): The width value to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute with validation

        Args:
            value (int): The height value to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle with print_symbol

        Returns:
            str: String representation of the rectangle, or empty string
            if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = getattr(self, 'print_symbol', Rectangle.print_symbol)

        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append(str(symbol) * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """Return a string representation that can recreate a new instance

        Returns:
            str: String representation in the format Rectangle(width, height)
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor method that prints message when instance is deleted"""
        Rectangle.number_of_instances -= 1  # Decrement counter
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger area

        Args:
            rect_1 (Rectangle): First rectangle to compare
            rect_2 (Rectangle): Second rectangle to compare

        Returns:
            Rectangle: The rectangle with bigger area, or rect_1 if equal

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle instance with equal width and height

        Args:
            size (int, optional): The size for both width and height.
            Defaults to 0.

        Returns:
            Rectangle: A new Rectangle instance with width == height == size
        """
        return cls(size, size)
