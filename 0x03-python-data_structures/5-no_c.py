#!/usr/bin/python3

def no_c(my_string):
    chars = len(my_string)
    buf = ""
    for i in range(0, chars):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        buf = buf + my_string[i]
    return buf
