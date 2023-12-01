#!/usr/bin/python3
"""Fetching URL """
import urllib.request


if __name__ == "__main__":
    fetched_url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(fetched_url) as url_read:
        read_content = url_read.read()
        file_type = read_content.decode('utf-8')
        resource_type = type(read_content)
        print(f"Body response:\n\t- type: {resource_type}\n\t\
- content: {read_content}\n\t- utf8 content: {file_type}")
