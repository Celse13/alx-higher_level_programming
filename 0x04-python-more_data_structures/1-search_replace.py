#!/usr/bin/python3
def search_replace(my_list, search, replace):
    modified_list = my_list[:]
    for element in modified_list:
        if element == search:
            element = replace
    return modified_list
