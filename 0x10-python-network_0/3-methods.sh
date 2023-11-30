#!/bin/bash
# Show the supported HTTP methods accepted by the server at a provided URL.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
