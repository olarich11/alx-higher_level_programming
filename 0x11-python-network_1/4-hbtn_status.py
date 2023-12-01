#!/usr/bin/python3
"""
Module that utilizes "request" library to fetch the status of https://intranet.hbtn.io.
"""
import requests


def main():
    """
    Function that fetches https://intranet.hbtn.io/status
    """
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))

if __name__ == "__main__":
    main()
