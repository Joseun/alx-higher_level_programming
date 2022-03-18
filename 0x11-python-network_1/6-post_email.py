#!/usr/bin/python3
"""  script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of the
    response
"""
import requests
from sys import argv


def post_emailr():
    """sends a POST request to the passed URL with the email as a parameter"""
    url = argv[1]
    values = {'email': argv[2]}
    r = requests.post(url, data=values)
    req = requests.get(argv[1])
    print(req.content)

if __name__ == "__main__":
    post_emailr()
