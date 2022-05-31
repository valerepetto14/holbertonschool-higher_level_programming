#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """def append_write"""
    with open(filename, 'a', encoding="utf-8") as f:
        num_bytes = f.write(text)
    return num_bytes
