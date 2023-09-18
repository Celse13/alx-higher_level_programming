#!/usr/bin/python3
"""Base class representation and importation of different modules."""
import json
import csv


class Base:
    """Representation of the class of Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Id initializer"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returning the json representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writing json string representation to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as writting_file:
            if list_objs is None:
                writting_file.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                writting_file.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Return json represantation string."""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returning instance will all attributes set."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        else:
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """"Returning the list of instances."""
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as read_file:
                list_dicts = Base.from_json_string(read_file.read())
                return [cls.create(**dicts) for dicts in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV."""
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    filed_names = ["id", "width", "height", "x", "y"]
                else:
                    filed_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=filed_names)
                for objct in list_objs:
                    writer.writerow(objct.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loading from the csv file to python object."""
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                dicts_list = csv.DictReader(csvfile, fieldnames=field_names)
                dicts_list = [dict([key, int(value)]
                              for key, value in objct.items())
                              for objct in dicts_list]
                return [cls.create(**objct) for objct in dicts_list]
        except IOError:
            return []
