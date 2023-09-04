#!/usr/bin/python3
"""Define a class for rectangle."""


class Rectangle:
    """Representation of a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constuctor of attributes for a new Rectangle.
        Args:
            width (int): width of new instance width.
            height (int): height of new instance height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finding which rectangle is the largest.
        Args:
            rect_1 (Rectangle): rectangle one.
            rect_2 (Rectangle): rectangle two.
        Raises:
            TypeError: When rect_1 and rect_2 are not instance of rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Provide new class of rectangle.
        Args:
            size (int): size for width and height.
        """
        return (cls(size, size))

    def __str__(self):
        """Display a string representation of a reactangle."""
        if self.__width == 0 or self.__height == 0:
            return ('')
        n_w = []
        for i in range(self.__height):
            [n_w.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                n_w.append("\n")
        return ("".join(n_w))

    def __repr__(self):
        """Display a strigng representation of a reactangle."""
        printaable_output = "Rectangle(" + str(self.__width)
        printaable_output += ", " + str(self.__height) + ")"
        return (printaable_output)

    def __del__(self):
        """Display a message after deleting rectangle instance."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
