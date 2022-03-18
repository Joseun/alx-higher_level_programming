#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8)
"""
import requests
from urllib.error import URLError, HTTPError
from sys import argv


def error_rcode():
    """ sends a request to the URL and displays the body of the response """
    try:
        response = requests.get(argv[1])
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('Error code: ', e.response.status_code)
    except requests.exceptions.ConnectionError as e:
        print('Index')
    else:
        print(response.content)

if __name__ == "__main__":
    error_rcode()
