#!/usr/bin/python3
"""  script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


def json_api():
    """sends a POST request to the passed URL with a letter as a parameter"""
    url = "http://0.0.0.0:5000/search_user"
    if !argv[1]:
        values = {'q': ""}
    else:
        values = {'q': argv[1]}
    r = requests.post(url, data=values)
    req = requests.get(url)
    try:
        req.json()
    except requests.exceptions.JSONDecodeError:
        print ("Not a valid JSON")
    else:
        if req.status_code == 204:
            print ("No result")
        else:
            print ('[{}] {}'.format(req.content.id, req.content.name))

if __name__ == "__main__":
    json_api()
