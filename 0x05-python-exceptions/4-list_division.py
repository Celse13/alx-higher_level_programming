#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for index in range(list_length):
            try:
                num_one = my_list_1[index]
                num_two = my_list_2[index]
                result = num_one / num_two
                new_list += result
            except TypeError:
                print("wrong type")
                new_list += 0
            except ZeroDivisionError:
                print("division by 0")
                new_list += 0
            except IndexError:
                print("out of range")
                new_list += 0
    finally:
        return (new_list)
