#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    first_set = set(set_1)
    second_set = set(set_2)
    all_element = first_set ^ second_set
    return all_element
