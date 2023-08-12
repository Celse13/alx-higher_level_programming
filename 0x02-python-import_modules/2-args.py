#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    word = "argument"
    arguments_from_pipe = argv[1:]
    length = len(arguments_from_pipe)

    if length == 0:
        word += "s."
        print("{} {}".format(length, word))
    elif length == 1:
        word += ":"
        print("{} {}".format(length, word))
    else:
        word += "s:"
        print("{} {}".format(length, word))

    for i in range(length):
        print("{}: {}".format(i + 1, arguments_from_pipe[i]))
