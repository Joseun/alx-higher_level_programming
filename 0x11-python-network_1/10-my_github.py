#!/usr/bin/python3
"""  sscript that takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id
"""
import requests
from sys import argv


def my_github():
    """sends a POST request to the passed URL with a letter as a parameter"""
    url = "https://api.github.com/user"
    print(argv[1], argv[2])
    values = {argv[1]: argv[2]}
    req = requests.get(url, params=values)
    try:
        req.json()
    except requests.exceptions.JSONDecodeError:
        print ("Not a valid JSON")
    else:
        if req.status_code == 404:
            print ("None")
        else:
            print (req.content)

if __name__ == "__main__":
    my_github()
