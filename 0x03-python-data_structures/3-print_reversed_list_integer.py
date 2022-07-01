#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    items = len(my_list) - 1

    for item in range(items, -1, -1):
        print("{:d}".format(my_list[item]))
