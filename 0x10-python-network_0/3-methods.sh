#!/bin/bash
# a Script that cURL only methods
curl -sI "$1" | grep "Allow:" | cut -f2- -d' '
