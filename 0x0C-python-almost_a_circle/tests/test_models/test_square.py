#!/usr/bin/python3
"""Unit testing development for the Square class.
    Importing the testing modules to handle test cases
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInitialization(unittest.TestCase):
    """Initialization of the class of Square."""
    def test_1(self):
        """Initialization of the class of Square."""
        self.assertIsInstance(Square(2), Base)

    def test_2(self):
        """Initialization of the class of Square."""
        self.assertIsInstance(Square(2), Square)

    def test_3(self):
        """Initialization of the class of Square."""
        with self.assertRaises(TypeError):
            Square()

    def test_4(self):
        """Checking with single argument."""
        square_1 = Square(5)
        square_2 = Square(6)
        self.assertEqual(square_1.id, square_2.id - 1)

    def test_5(self):
        """Checking with two arguments."""
        square_1 = Square(7, 8)
        square_2 = Square(11, 12)
        self.assertEqual(square_1.id, square_2.id - 1)


class TestSize(unittest.TestCase):
    """Checking for the size."""
    def test_size_1(self):
        """Checking for the size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_size_2(self):
        """Checking for the size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("celse")

    def test_size_3(self):
        """Checking for the size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(0.3)


class TestX(unittest.TestCase):
    """Testing the size of x."""
    def test_x_1(self):
        """Testing the size of x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_x_2(self):
        """Testing the size of x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "celse")

    def test_x_3(self):
        """Testing the size of x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 0.3)

    def test_x_4(self):
        """Testing the size of x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, complex(4))

    def test_x_5(self):
        """Testing the size of x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"x": 4, "y": 2}, 3)


class TestY(unittest.TestCase):
    """Testing the size of y."""
    def test_y_1(self):
        """Testing the size of y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(6, 5, None)

    def test_y_2(self):
        """Testing the size of y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "celse")

    def test_y_3(self):
        """Testing the size of y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, 2.3)

    def test_y_4(self):
        """Testing the size of y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 8, complex(10))

    def test_y_5(self):
        """Testing the size of y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 5, {"x": 8, "y": 5})
