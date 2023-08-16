#!/usr/bin/python3
def weight_average(my_list=[]):
    up_fraction = 0
    down_fraction = 0
    if my_list:
        for element in my_list:
            up_fraction += element[0] * element[1]
            down_fraction += element[1]
        operation = up_fraction / down_fraction
        return operation
    else:
        return 0
