#!/usr/bin/python3
"""asd asd asd"""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    load = load_from_json_file(filename)
except FileNotFoundError:
    load = []

save_to_json_file(load + argv[1:], filename)