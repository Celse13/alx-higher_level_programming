#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    modified_dict = {}
    for element in a_dictionary:
        modified_dict[element] = a_dictionary[element] * 2
    return (modified_dict)
