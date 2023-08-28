#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return_value = a / b
    except ZeroDivisionError:
        return (None)
    finally:
        print("Inside result: {}".format(return_value))
    return (return_value)
