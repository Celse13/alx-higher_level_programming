#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    word = "argument"
    arguments_from_pipe = argv[1:]
    length = len(arguments_from_pipe)
    if length == 0:
        word += "s"
        print(f"{length} {word}")
    elif length == 1:
        word += ":"
        print(f"{length} {word}")
    else:
        word += "s:"
        print(f"{length} {word}")
    for i in range(length):
        print(f"{i + 1}: {arguments_from_pipe[i]}")
