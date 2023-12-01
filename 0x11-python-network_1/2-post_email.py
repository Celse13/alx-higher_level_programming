#!/usr/bin/python3
"""script"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    read_url = sys.argv[1]
    read_email = sys.argv[2]
    temp = {"email": read_email}
    utf_read = urllib.parse.urlencode(temp).encode('utf-8')
    request = urllib.request.Request(read_url, data=utf_read, method='POST')
    with urllib.request.urlopen(request) as rqst:
        print(rqst.read().decode('utf-8'))
