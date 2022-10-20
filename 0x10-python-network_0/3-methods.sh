#!/bin/bash
# displays all HTTP methods the server will accept
curl -sI "$1" | grep "Allow" | sed 's/Allow: //g'
