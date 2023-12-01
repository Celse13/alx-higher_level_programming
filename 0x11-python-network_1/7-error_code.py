#!/usr/bin/python3
"""script"""
import requests
import sys


if __name__ == "__main__":
    read_url = sys.argv[1]
    resource = requests.get(read_url)
    if (resource.status_code >= 400):
        print(f"Error code: {resource.status_code}")
        exit()
    print(resource.text)
