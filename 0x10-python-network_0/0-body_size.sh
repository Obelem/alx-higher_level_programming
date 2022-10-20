#!/bin/bash
# sends a request to a URL and displays size of body response
curl -sI 0.0.0.0:5000 | grep -i Content-Length | cut -d " " -f2
