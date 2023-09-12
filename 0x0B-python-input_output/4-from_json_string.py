#!/usr/bin/python3
"""Importing json module to handle json functionality."""
from json import loads


def from_json_string(my_str):
    """Return Python object representation of my_obj."""

    return (loads(my_str))
