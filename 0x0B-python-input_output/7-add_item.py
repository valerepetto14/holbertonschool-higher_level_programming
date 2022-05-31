#!/usr/bin/python3
"""
Write a script that adds all arguments
to a Python list, and then save them to a file:
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = 'add_item.json'
try:
    object = load_from_json_file(file)
except FileNotFoundError:
    object = []

save_to_json_file(object + argv[1:], file)

