#!/bin/bash
# Issue a GET request to a specified URL and show the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
