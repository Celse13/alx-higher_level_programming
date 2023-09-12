#!/usr/bin/python3
"""Function that will write content to the file and print read characters."""


def write_file(filename="", text=""):
    """Writing string to the text file."""

    with open(filename, 'w', encoding='utf-8') as read_file:
        read_characters = read_file.write(text)
        return (read_characters)
