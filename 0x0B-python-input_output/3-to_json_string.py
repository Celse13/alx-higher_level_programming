#!/usr/bin/python3
"""Importing json module to handle json functionality."""
from json import dumps


def to_json_string(my_obj):
    """Return json representation of my_obj."""

    return (dumps(my_obj))
