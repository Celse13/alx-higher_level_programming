#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count_element = 0
    try:
        for index in range(x):
            print(my_list[index], end='')
            count_element += 1
    except IndexError:
        None
    print()
    return (count_element)
