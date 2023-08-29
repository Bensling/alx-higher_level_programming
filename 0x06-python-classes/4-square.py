#!/usr/bin/python3

"""
Square Module.

This module defines a Square class for working with square shapes. It includes methods
for setting and getting the size of the square, along with a method to calculate the
area of the square.
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
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be non-negative")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
