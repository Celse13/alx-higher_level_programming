#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_to_be_sorted = sorted(a_dictionary.keys())
    for i in range(len(keys_to_be_sorted)):
        key = keys_to_be_sorted[i]
        value = a_dictionary[key]
        print("{}, {}".format(key, value))
