#!/usr/bin/python3

def element_at(my_list, idx):
    items = len(my_list) - 1

    if idx < 0 or idx > items:
        return None
    else:
        return my_list[idx]
