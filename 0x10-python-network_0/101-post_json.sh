#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
# script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
curl -s "$1" -X POST -d @"$2".json -H "Content-Type: application/json" 
curl -s "$1"
