#!/usr/bin/python3
"""script"""
import requests


if __name__ == "__main__":
    read_url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(read_url)
    content = response.text
    response_type = type(content)
    print(f"Body response:\n\t- type: {response_type}\n\t\
- content: {content}")
