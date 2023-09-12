#!/usr/bin/python3
"""Function that will read content from file and print to stdout."""


def read_file(filename=""):
    """Reading content and printing to stdout."""

    with open(filename, 'r', encoding='utf-8') as read_file:
        file_contents = read_file.read()
        print(file_contents, end='')
