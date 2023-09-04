#!/usr/bin/python3
"""Define a class for rectangle."""


class Rectangle:
    """Representation of a rectangle."""

    def __init__(self, width=0, height=0):
        """Constuctor of attributes for a new Rectangle.
        Args:
            width (int): width of new instance width.
            height (int): height of new instance height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieving the value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieving the value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the are of a rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Compute the perimeter of a Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Display a string representation of a reactangle."""
        if self.__width == 0 or self.__height == 0:
            return ('')

        printaable_output = []
        for i in range(self.__height):
            row = ['#' for j in range(self.__width)]
            row_str = ''.join(row)
            printaable_output.append(row_str)
            if i != self.__height - 1:
                printaable_output.append("\n")
        return (''.join(printaable_output))
