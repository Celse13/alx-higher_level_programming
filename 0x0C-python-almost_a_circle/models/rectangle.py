#!/usr/bin/python3
"""Representation of Base class."""


from models.base import Base


class Rectangle(Base):
    """Representation of the class of rectangle.

     Attributes:
        width (int): rectangle width instance variable.
        height (int): rectangle height instance variable.
        x (int): rectangle x instance variable
        y (int): rectangle y instance variable
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initalization of the new rectangle.

        Args:
            width (int): rectangle width instance variable..
            height (int): rectangle height instance variable.
            x (int): rectangle x instance variable.
            y (int): rectangle y instance variable.
            id (int): Rectangle instance Id.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Displaying the rectangle"""
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    @property
    def width(self):
        """Retrieving the width of rectangle.

        Returns:
            int: size of the width of rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the value of width.

        Args:
            value (int): new size of the rectangle.

        Raises:
            TypeError: when the width is not instance of int.
            ValueError: if value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieveing the value of the height.

        Returns:
            int: new size of the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Settting the value of new height.

        Args:
            value (int): new height size.

        Raises:
            TypeError: When height is not instance of height.
            ValueError: when height is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieving the value of x.

        Returns:
            int: the size of x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setting the value of x.

        Args:
            value (int): the new size of new x.

        Raises:
            TypeError: When x is not an instance of int.
            ValueError: When x < 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieving the value of y.

        Returns:
            int: the size of y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setting the value of y.

        Args:
            value (int): new value of the y.

        Raises:
            TypeError: When y is not an instance of int.
            ValueError: when y < 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computing the value of area for the instance for rectangle.

        Returns:
            int: Area of the rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """Printing Rectangle instance with the character # at stdout."""
        display_rectangle = ""
        print("\n" * self.y, end='')
        for i in range(self.height):
            display_rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(display_rectangle, end='')

    def update(self, *args, **kwargs):
        """Dealing with extra positional arguments and key value pairs.

        Args:
            *args (tuple): extra args.
            **kwargs (dict): extra key/value args.
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returning the dictionary representation of the rectangle.

        Returns:
            dict: Setting the new rectangle
        """
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}
