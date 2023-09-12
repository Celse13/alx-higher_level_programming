#!/usr/bin/python3
"""Adds command-line arguments to a Python list,
saves it to 'add_item.json',
and loads it back..
"""
from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        current_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        current_list = []
    current_list.extend(argv[1:])

    save_to_json_file(current_list, "add_item.json")
