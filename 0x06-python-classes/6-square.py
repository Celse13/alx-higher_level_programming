#!/usr/bin/python3
"""Definition of a Square class."""


class Square:
    """Representation of a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor for the square class.
        Args:
            size (int): size private attribute.
            position (int, int): new posistion for instance
        """
        self.__size = size
        self.position = position

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
    @property
    def position(self):
        """Retrieve the position."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Displaying square of position with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for u in range(self.__position[1])]
        for u in range(self.__size):
            [print(" ", end="") for v in range(self.__position[0])]
            [print("#", end="") for w in range(self.__size)]
            print("")
