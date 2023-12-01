#!/usr/bin/python3
""" module doc """
import requests
import sys


if __name__ == "__main__":
    read_url = sys.argv[1]
    read_email = sys.argv[2]
    temp = {"email": read_email}
    resource = requests.post(read_url, data=temp)
    print(resource.text)
