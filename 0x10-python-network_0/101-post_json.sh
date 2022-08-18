#!/bin/bash
#Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -X POST "$1" 'Content-Type: application/json'-d '{"name": "John Doe",  "age": 33}'
