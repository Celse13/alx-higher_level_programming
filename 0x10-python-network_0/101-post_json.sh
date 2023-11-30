#!/bin/bash
# A script that cURL a JSON file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
