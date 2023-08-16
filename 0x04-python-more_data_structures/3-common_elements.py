#!/usr/bin/python3
def common_elements(set_1, set_2):
    first_set = set(set_1)
    second_set = set(set_2)
    inter_element = first_set.intersection(second_set)
    return (inter_element)
