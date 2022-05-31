#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    Function to read a file and print it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)