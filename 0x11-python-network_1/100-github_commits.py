#!/usr/bin/python3
"""script"""
from requests import get
from sys import argv


if __name__ == "__main__":
    ad = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    com = get(ad).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                com[i].get("sha"),
                com[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
