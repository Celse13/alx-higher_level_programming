def max_integer(my_list=[]):
    if not my_list:
        return None
    maximum_val = my_list[0]
    for n in range(1, len(my_list)):
        if my_list[n] > maximum_val:
            maximum_val = my_list[n]
    return (maximum_val)
