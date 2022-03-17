#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
SC="$(curl -s -i  "$1"| head -1 | awk '{print $2}')"
if [ "$SC" -eq 200 ]
    then
        "$(curl -sL "$1")"
fi
