#!/usr/bin/python3
"""script"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        first_arg = sys.argv[1]
    else:
        first_arg = ""
    address = "http://0.0.0.0:5000/search_user"
    temp = {"q": first_arg}
    resource = requests.post(address, data=temp)
    try:
        resourcejs = resource.json()
        if resourcejs:
            print(f'[{resourcejs["id"]}] {resourcejs["name"]}')
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
