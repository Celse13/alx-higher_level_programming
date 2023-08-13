#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for integer in reversed(range(len(my_list))):
        print("{:d}".format(my_list[integer]))
