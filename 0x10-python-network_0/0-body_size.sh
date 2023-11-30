#!/bin/bash
# Determine the size of the HTTP response header in bytes for a specified URL.
curl -s "$1" | wc -c
