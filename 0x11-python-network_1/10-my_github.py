#!/usr/bin/python3
"""script"""
import requests
from sys import argv


if __name__ == "__main__":
    x = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(x.json().get('id'))
