#!/usr/bin/python3
"""Creating object from the json file."""
from json import load


def load_from_json_file(filename):
    """Object from json file."""

    with open(filename) as read_file:
        return (load(read_file))
