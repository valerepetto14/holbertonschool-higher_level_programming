#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file,
after each line containing a specific string (see example):
"""


def append_after(filename="", search_string="", new_string=""):
    """def append_after"""
    new_text = ""
    with open(filename, 'r') as f:
        for linea in f:
            new_text += linea
            if search_string in linea:
                new_text += new_string

    with open(filename, 'w') as f:
        f.write(new_text)
