#!/usr/bin/python3
# 1-rectangle.py
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
