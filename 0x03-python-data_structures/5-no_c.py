#!/usr/bin/python3
def no_c(my_string):
    char_holder = ""
    for character in my_string:
        if character == "c" or character == "C":
            continue
        char_holder += character
    return char_holder
