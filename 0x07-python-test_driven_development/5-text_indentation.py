#!/usr/bin/python3
"""Defines a function that prints a text with 2
new lines after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """This function performs the indentation of the given text.
    Args:
        text (string): text to be printed.
    Raises:
        TypeError: When (text) is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    is_block_whitespace = False
    special_char = ['.', '?', ':']
    for char in text:
        if char in special_char:
            new_text += char + "\n\n"
            is_block_whitespace = True
        else:
            if char.isspace():
                if is_block_whitespace:
                    continue
                else:
                    new_text += "\n"
                    is_block_whitespace = True
            else:
                new_text += char
                is_block_whitespace = False
    print(new_text, end='')
