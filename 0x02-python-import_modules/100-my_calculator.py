#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import div, add, sub, mul
    from sys import argv
    length = len(argv[1:])

    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[0])
    b = int (argv[2])
    
    if argv[1] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[1] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif argv[1] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif argv[1] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
