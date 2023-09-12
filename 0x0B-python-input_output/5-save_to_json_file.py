#!/usr/bin/python3
"""Writing object to the text_file usign json."""
from json import dumps


def save_to_json_file(my_obj, filename):
    """Writing object to text file using json representation."""

    with open(filename, 'w') as read_file:
        read_file.write(dumps(my_obj))
