#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
email="test@gmail.com"
sub="I will always be here for PLD"
curl -s -X POST -d "email=$email&subject=$sub" "$1"
