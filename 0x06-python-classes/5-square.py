#!/usr/bin/python3
"""Definition of a Square class."""


class Square:
    """Representation of a square."""

    def __init__(self, size=0):
        """Constructor for the square class.
        Args:
            size (int): size private attribute.
        """
        self.__size = size

    @property
    def size(self):
        """Retriving the value of size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setting the value of size.
        Args:
        value (int): setting value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Displaying the square with #"""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
