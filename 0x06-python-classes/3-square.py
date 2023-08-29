#!/usr/bin/python3

"""
Square Utility Module.

This module defines a class for working with squares. It includes an initialization
method to set the square's size while ensuring valid input, and a method to calculate
the area of the square.
"""

class Square:
    """
    Represents a square shape.
    """
    def __init__(self, size=0):
        """
        Initializes the square object.

        Args:
            size (int): The length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be non-negative")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
