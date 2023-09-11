#!/usr/bin/python3
"""Dynamic importation of Rectangle Class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of Square."""
    def __init__(self, size):
        """Initializer for size"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return("[Square] " + str(self.__size) + "/" + str(self.__size))
