#!/usr/bin/python3
def search_replace(my_list, search, replace):
    modified_list = list()
    modified_list = my_list[:]
    for n in range(len(modified_list)):
        if modified_list[n] == search:
            modified_list[n] = replace
    return modified_list
