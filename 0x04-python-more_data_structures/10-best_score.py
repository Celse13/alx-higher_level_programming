#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_value = list(a_dictionary.keys())[0]
        for key, value in a_dictionary.items():
            if value > a_dictionary[max_value]:
                max_value = key
        return max_value
