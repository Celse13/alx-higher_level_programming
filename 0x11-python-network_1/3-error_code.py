#!/usr/bin/python3
""" module doc """
import urllib.request
import sys


if __name__ == "__main__":
    try:
        read_url = sys.argv[1]
        with urllib.request.urlopen(read_url) as fl:
            print(fl.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
