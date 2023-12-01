#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL"""
import urllib.request
import sys

if __name__ == "__main__":
    read_url = sys.argv[1]
    with urllib.request.urlopen(read_url) as read_response:
        print(read_response.info()["X-Request-Id"])
