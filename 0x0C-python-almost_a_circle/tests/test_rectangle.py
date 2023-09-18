#!/usr/bin/python3
"""Unit testing development for the Rectangle class.
    Importing the testing modules to handle test cases
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangleMethods(unittest.TestCase):
    """Class to test Rectangle class methods."""

    def setUp(self):
        """Set up test instances."""
        self.rectangle = Rectangle(2, 3)

    def test_rectangle_init(self):
        """Test Rectangle initialization."""
        self.assertEqual(self.rectangle.width, 2)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.x, 0)
        self.assertEqual(self.rectangle.y, 0)

    def test_area(self):
        """Test calculation of area."""
        self.assertEqual(self.rectangle.area(), 6)

    def test_rectangle_for_instance(self):
        """Test Rectangle initialization."""
        self.assertIsInstance(Rectangle(16, 35), Base)

    def test_for_no_arguments(self):
        """Test Rectangle initialization."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_for_one_argument(self):
        """Test Rectangle initialization."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_for_id_1(self):
        """Test Rectangle initialization."""
        rect_1 = Rectangle(16, 35)
        rect_2 = Rectangle(16, 35)
        self.assertEqual(rect_1.id, rect_2.id - 1)

    def test_for_id_2(self):
        """Test Rectangle initialization."""
        rect_1 = Rectangle(16, 35, 28)
        rect_2 = Rectangle(416, 35, 28)
        self.assertEqual(rect_1.id, rect_2.id - 1)

    def test_for_id_3(self):
        """Test Rectangle initialization."""
        rect_1 = Rectangle(16, 35, 28, 9)
        rect_2 = Rectangle(16, 35, 28, 9)
        self.assertEqual(rect_1.id, rect_2.id - 1)


class TestWidth(unittest.TestCase):
    """Testing for the width."""
    def test_for_width_1(self):
        """Testing for the width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4)

    def test_for_width_2(self):
        """Testing for the width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 4)

    def test_for_width_3(self):
        """Testing for the width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(6.3, 4)

    def test_for_width_4(self):
        """Testing for the width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"x": 5, "y": 4}, 4)

    def test_for_width_5(self):
        """Testing for the width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 4)

    def test_for_width_6(self):
        """Testing for the width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([4, 5, 9], 5)

    def test_for_width_7(self):
        """Testing for the width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({4, 5, 9}, 9)

    def test_for_width_8(self):
        """Testing for the width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((4, 5, 9), 7)


class TestHeight(unittest.TestCase):
    """Testing for the height."""
    def test_for_height_1(self):
        """Testing for the height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, None)

    def test_for_height_2(self):
        """Testing for the height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "celse")

    def test_for_height_3(self):
        """Testing for the height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, 6.3)

    def test_for_height_4(self):
        """Testing for the height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {"x": 5, "y": 4})

    def test_for_height_5(self):
        """Testing for the height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, False)

    def test_for_height_6(self):
        """Testing for the height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, [4, 5, 9])

    def test_for_height_7(self):
        """Testing for the height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {4, 5, 9})

    def test_for_height_8(self):
        """Testing for the height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, (4, 5, 9))


class TestX(unittest.TestCase):
    """Testcase for x."""
    def test_x_1(self):
        """Testcase for x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, None)

    def test_x_2(self):
        """Testcase for x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, "celse", 5)

    def test_x_3(self):
        """Testcase for x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, 4.8, 9)

    def test_x_4(self):
        """Testcase for x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, complex(9))

    def test_x_4(self):
        """Testcase for x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, {"x": 1, "v": 5}, 7)

    def test_x_5(self):
        """Testcase for x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, True, 2)


class TestY(unittest.TestCase):
    """Testing the y attribute."""
    def test_y_1(self):
        """Testing the y attribute."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 7, None)

    def test_y_2(self):
        """Testing the y attribute."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 7, "celse")

    def test_y_3(self):
        """Testing the y attribute."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 7, 5.5)

    def test_y_4(self):
        """Testing the y attribute."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 7, complex(5))

    def test_y_5(self):
        """Testing the y attribute."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 7, {"x": 1, "y": 2})

    def test_y_6(self):
        """Testing the y attribute."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 7, [5, 6, 7])

    def test_y_7(self):
        """Testing the y attribute."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 7, {5, 6, 7})

    def test_y_8(self):
        """Testing the y attribute."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 7, (5, 6, 7))
