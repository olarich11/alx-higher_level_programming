#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
import requests
from sys import argv


def main(argv):
    """
    Send a POST request to the provided URL with the email as a parameter
    and show the decoded UTF-8 body of the response.
    """
    values = {'email': argv[2]}
    url = argv[1]
    r = requests.post(url, data=values)
    print(r.text)

if __name__ == "__main__":
    main(argv)
