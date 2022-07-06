#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_list.sort()
    add = my_list[0]
    if len(my_list) == 1:
        return add

    for i in range(1, len(my_list)):
        if my_list[i] != my_list[i - 1]:
            add = add + my_list[i]
    return add
