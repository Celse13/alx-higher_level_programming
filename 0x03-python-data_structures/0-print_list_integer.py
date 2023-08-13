#!/usr/bin/python3
def print_list_integer(my_list=[]):
    length_for_str = len(my_list)
    for integer in range(length_for_str):
        print("{}".format(my_list[integer]))
