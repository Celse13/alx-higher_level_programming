#!/usr/bin/python3
"""script"""
import requests
import sys


if __name__ == "__main__":
    read_url = sys.argv[1]
    response = requests.get(read_url)
    print(response.headers.get("X-Request-Id"))
