#!/usr/bin/python3
"""Unit testing development for the base class.
    Importing the testing modules to handle test cases
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInitialization(unittest.TestCase):
    """Performing unittest for the base class."""

    def test_missing_argument(self):
        """Testing the provided id."""
        instance_one = Base()
        instance_two = Base()
        self.assertEqual(instance_one.id, instance_two.id - 1)

    def test_more_constructor(self):
        """Testing the provided id."""
        instance_one = Base()
        instance_one = Base()
        instance_two = Base()
        instance_three = Base()
        instance_four = Base()
        self.assertEqual(instance_three.id, instance_four.id - 1)

    def test_id(self):
        """Testing the provided id."""
        instance_one = Base()
        instance_one = Base(None)
        instance_two = Base(None)
        self.assertEqual(instance_one.id, instance_two.id - 1)

    def test_id_two(self):
        """Testing the provided id."""
        instance_one = Base(89)
        self.assertEqual(instance_one.id, 89)

    def test_id_three(self):
        """Testing the provided id."""
        instance_one = Base(5.3)
        self.assertEqual(instance_one.id, 5.3)

    def test_id_four(self):
        """Testing the provided id."""
        instance_one = Base(True)
        self.assertEqual(instance_one.id, True)

    def test_id_five(self):
        """Testing the provided id."""
        instance_one = Base([89, 23, 82])
        self.assertEqual(instance_one.id, [89, 23, 82])

    def test_id_six(self):
        """Testing the provided id."""
        instance_one = Base((23, 28))
        self.assertEqual(instance_one.id, (23, 28))

    def test_id_seven(self):
        """Testing the provided id."""
        instance_one = Base(float('inf'))
        self.assertEqual(instance_one.id, float('inf'))

    def test_id_eight(self):
        """Testing the provided id."""
        instance_one = Base(range(28))
        self.assertEqual(instance_one.id, range(28))


class TestJsonForAllObject(unittest.TestCase):
    """Performing json Test for (Rectangle and Square)."""
    def test_json_object_rectangle(self):
        """Testing json object."""
        rect_1 = Rectangle(16, 53, 6, 17, 18)
        self.assertEqual(type(Base.to_json_string([rect_1.to_dictionary()])),
                         str)

    def test_json_object_square(self):
        """Testing json object."""
        square_1 = Square(16, 6, 17, 18)
        self.assertEqual(type(Base.to_json_string([square_1.to_dictionary()])),
                         str)

    def test_json_object_square_for_empty(self):
        """Testing json object."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_json_object_square_for_none(self):
        """Testing json object."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_json_object_for_no_arguments(self):
        """Testing json object."""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_json_object_for_extra_arguments(self):
        """Testing json object."""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_json_object_for_extra_arguments_two_dicts(self):
        """Testing json object."""
        square_1 = Square(11, 15, 3, 45)
        square_2 = Square(44, 7, 25, 4)
        new_list = [square_1.to_dictionary(), square_2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(new_list)) == 81)

    def test_json_object_for_extra_arguments_one_dicts(self):
        """Testing json object."""
        square_1 = Square(11, 15, 3, 45)
        new_list = [square_1.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(new_list)) == 41)


class TestBaseSavingFiles(unittest.TestCase):
    """"Dealing with saving files."""

    def test_saving_file_to_a_rectangle(self):
        """Saving to rectangle."""
        rect_1 = Rectangle(45, 77, 21, 81, 65)
        Rectangle.save_to_file([rect_1])
        with open("Rectangle.json", "r") as read_file:
            self.assertTrue(len(read_file.read()) == 57)

    def test_saving_file_for_two_rectangles(self):
        """Saving to file."""
        rect_1 = Rectangle(41, 27, 15, 58, 65)
        rect_2 = Rectangle(41, 27, 15, 58, 65)
        Rectangle.save_to_file([rect_1, rect_2])
        with open("Rectangle.json", "r") as read_file:
            self.assertTrue(len(read_file.read()) == 114)

    def test_saving_file_to_a_one_square(self):
        """Saving to file."""
        square_1 = Square(41, 27, 15, 58)
        Square.save_to_file([square_1])
        with open("Square.json", "r") as read_file:
            self.assertTrue(len(read_file.read()) == 42)

    def test_saving_file_to_a_two_square(self):
        """Saving to file."""
        square_1 = Square(41, 27, 15, 58)
        square_2 = Square(41, 27, 15, 58)
        Square.save_to_file([square_1, square_2])
        with open("Square.json", "r") as read_file:
            self.assertTrue(len(read_file.read()) == 84)

    def test_saving_file_to_a_one_base(self):
        """Saving to file."""
        square_1 = Square(41, 27, 15, 58)
        Base.save_to_file([square_1])
        with open("Base.json", "r") as read_file:
            self.assertTrue(len(read_file.read()) == 42)

    def test_saving_file_to_a_square(self):
        """Saving to file."""
        square_1 = Square(41, 27, 15, 58)
        Square.save_to_file([square_1])
        square_1 = Square(41, 27, 15, 58)
        Square.save_to_file([square_1])
        with open("Square.json", "r") as read_file:
            self.assertTrue(len(read_file.read()) == 42)

    def test_saving_file_to_a_square_None(self):
        """Saving to file."""
        Square.save_to_file(None)
        with open("Square.json", "r") as read_file:
            self.assertEqual(read_file.read(), "[]")

    def test_saving_file_to_a_square_empty_list(self):
        """Saving to file."""
        Square.save_to_file([])
        with open("Square.json", "r") as read_file:
            self.assertEqual(read_file.read(), "[]")

    def test_saving_file_to_a_rectangle_no_arguments(self):
        """Saving to file."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_saving_file_to_a_rectangle_extra_arguments(self):
        """Saving to file."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 2)


class TestLoadJsonString(unittest.TestCase):
    """Loading from json files to Python object."""

    def test_loads_type(self):
        new_object = [{"id": 56, "width": 20, "height": 14}]
        json_new_object = Rectangle.to_json_string(new_object)
        created_object = Rectangle.from_json_string(json_new_object)
        self.assertEqual(list, type(created_object))

    def test_loads_equality(self):
        """Loading from json files to Python object."""
        new_object = [{"id": 56, "width": 20, "height": 14}]
        json_new_object = Rectangle.to_json_string(new_object)
        created_object = Rectangle.from_json_string(json_new_object)
        self.assertEqual(new_object, created_object)

    def test_loads_for_comparision(self):
        """Loading from json files to Python object."""
        new_object = [
            {"id": 56, "width": 20, "height": 14},
            {"id": 56, "width": 20, "height": 14}
        ]
        json_new_object = Rectangle.to_json_string(new_object)
        created_object = Rectangle.from_json_string(json_new_object)
        self.assertEqual(new_object, created_object)

    def test_loads_square_equality(self):
        """Loading from json files to Python object."""
        new_object = [{"id": 56, "size": 20, "height": 14}]
        json_new_object = Square.to_json_string(new_object)
        created_object = Square.from_json_string(json_new_object)
        self.assertEqual(new_object, created_object)

    def test_loads_for_square_comparision(self):
        """Loading from json files to Python object."""
        new_object = [
            {"id": 56, "size": 20, "height": 14},
            {"id": 56, "size": 20, "height": 14}
        ]
        json_new_object = Rectangle.to_json_string(new_object)
        created_object = Rectangle.from_json_string(json_new_object)
        self.assertEqual(new_object, created_object)

    def test_loads_None(self):
        """Loading from json files to Python object."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_loads_empty_list(self):
        """Loading from json files to Python object."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_loads_no_argument(self):
        """Loading from json files to Python object."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_loads_more_than_one_arg(self):
        """Loading from json files to Python object."""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 2)


class TestBaseCreate(unittest.TestCase):
    """"Testing the creation of different files."""

    def test_rectangle_creation(self):
        """"Testing the creation of different files."""
        rect_1 = Rectangle(3, 5, 1, 2, 7)
        rect_1_dict = rect_1.to_dictionary()
        new_rect = Rectangle.create(**rect_1_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect_1))

    def test_rectangle_was_created(self):
        """"Testing the creation of different files."""
        rect_1 = Rectangle(3, 5, 1, 2, 7)
        new_rect = rect_1.to_dictionary()
        rect_2 = Rectangle.create(**new_rect)
        self.assertIsNot(rect_1, rect_2)

    def test_rectangle_are_equal(self):
        """"Testing the creation of different files."""
        rect_1 = Rectangle(3, 5, 1, 2, 7)
        new_rect = rect_1.to_dictionary()
        rect_2 = Rectangle.create(**new_rect)
        self.assertNotEqual(rect_1, rect_2)

    def test_square_creation(self):
        """"Testing the creation of different files."""
        square_1 = Square(3, 5, 1, 7)
        square_dict = square_1.to_dictionary()
        square_2 = Square.create(**square_dict)
        self.assertEqual("[Square] (7) 5/1 - 3", str(square_1))

    def test_create_square_is(self):
        """"Testing the creation of different files."""
        square_1 = Square(2, 3, 4, 6)
        square_dict = square_1.to_dictionary()
        square_2 = Square.create(**square_dict)
        self.assertIsNot(square_1, square_2)


class TestBaseFileLoads(unittest.TestCase):
    """Loading from the file."""
    def test_load_for_rectangle(self):
        rect_1 = Rectangle(45, 77, 21, 81, 65)
        rect_2 = Rectangle(45, 77, 21, 81, 65)
        Rectangle.save_to_file([rect_1, rect_2])
        created_rectangle = Rectangle.load_from_file()
        self.assertEqual(str(created_rectangle[0]), str(rect_1))

    def test_load_for_rectangle_2(self):
        """Loading from the file."""
        rect_1 = Rectangle(45, 77, 21, 81, 65)
        rect_2 = Rectangle(45, 77, 21, 81, 65)
        Rectangle.save_to_file([rect_1, rect_2])
        create_rectangle = Rectangle.load_from_file()
        self.assertTrue(all(type(instance) == Rectangle for instance in
                            create_rectangle))

    def test_load_for_square(self):
        """Loading from the file."""
        square_1 = Square(11, 15, 3, 45)
        square_2 = Square(44, 7, 25, 4)
        Square.save_to_file([square_1, square_2])
        create_square = Square.load_from_file()
        self.assertEqual(str(create_square[0]), str(square_1))

    def test_load_for_square_1(self):
        """Loading from the file."""
        square_1 = Square(11, 15, 3, 45)
        square_2 = Square(44, 7, 25, 4)
        Square.save_to_file([square_1, square_2])
        create_square = Square.load_from_file()
        self.assertEqual(str(create_square[1]), str(square_2))


class TestBaseCsv(unittest.TestCase):
    """Testing for the cv file."""
    def test_create_csv_by_rectangle(self):
        rect_0 = Rectangle(2, 6, 4, 9, 1)
        Rectangle.save_to_file_csv([rect_0])
        with open("Rectangle.csv", "r") as read_file:
            self.assertTrue("1,9,4,6,2", read_file.read())

    def test_create_csv_by_square(self):
        s = Square(5, 6, 1, 3)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("3,5,6,1", f.read())


if __name__ == "__main__":
    unittest.main()
