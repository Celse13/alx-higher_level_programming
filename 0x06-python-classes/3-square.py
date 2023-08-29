#!/usr/bin/python3
"""Definition of a Square class."""


class Square:
    """Representation of a square."""

    def __init__(self, size=0):
        """Constructor for the square class.
        Args:
            size (int): size private attribute.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        """Computing the area of the square."""
        return (self.__size ** 2)
