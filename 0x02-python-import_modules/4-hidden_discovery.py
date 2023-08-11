#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for var in dir(hidden_4):
        if var[:2] != "__":
            print(var)
        else:
            exit()
    