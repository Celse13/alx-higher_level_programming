#!/usr/bin/python3
from sys import argv

arguments_from_pipe = argv[1:]
length = len(arguments_from_pipe)

summation = 0

for x in range(length):
    summation += int(arguments_from_pipe[x])
        
print(f"{summation}")
