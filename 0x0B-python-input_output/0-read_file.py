#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """def read file"""
    with open(filename, encoding="utf-8") as f:
        texto = f.read()
        print(texto, end="")
