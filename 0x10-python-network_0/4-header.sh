#!/bin/bash
# Perform a GET request to a specified URL with a custom header variable.
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
