#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = 0
    my_list_3 = []
    while n < list_length:
        return_value = 0
        try:
            return_value = my_list_1[n] / my_list_2[n]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndentationError:
            print("out of range")
        finally:
            my_list_3 += return_value
            n += 1
    return (my_list_3)
