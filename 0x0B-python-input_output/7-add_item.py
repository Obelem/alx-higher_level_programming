#!/usr/bin/python3
""" Module for task 7 """
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

FILENAME = "add_item.json"
args = sys.argv
args.pop(0)
try:
    items = load_from_json_file(FILENAME)
except FileNotFoundError as e:
    with open(FILENAME, "a") as f:
        f.write('[]\n')
    items = load_from_json_file(FILENAME)
items.extend(args)
save_to_json_file(items, FILENAME)
