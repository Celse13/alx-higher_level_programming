#!/bin/bash
# a Script hat cURL headers
curl -sI "$1" | grep "Allow:" | cut -f2- -d' '
