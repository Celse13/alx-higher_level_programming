#!/usr/bin/python3
"""Function that will write content to the file and print read characters."""


def append_write(filename="", text=""):
    """Appending string to the text file."""

    with open(filename, 'a', encoding='utf-8') as read_file:
        appended_char = read_file.write(text)
        return (appended_char)
