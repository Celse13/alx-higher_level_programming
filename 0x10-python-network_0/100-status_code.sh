#!/bin/bash
# A script for  Only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
