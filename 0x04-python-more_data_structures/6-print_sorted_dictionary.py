#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_to_be_sorted = sorted(a_dictionary)
    for i in keys_to_be_sorted:
        print("{}: {}".format(i, a_dictionary[i]))
