#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]

    new_tuple = (length, first_char)
    return new_tuple 
