#!/usr/bin/python3
"""Script"""
from requests import get
from sys import argv


if __name__ == "__main__":
    address = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    com = get(address).json()
    try:
        for i in range(1, 10, 1):
            print("{}: {}".format(
                com[i].get("sha"),
                com[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
