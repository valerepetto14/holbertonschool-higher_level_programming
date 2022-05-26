#!/usr/bin/python3
"""
function text_identation
"""


from hashlib import new


def text_indentation(text):
    """def function"""
    result = ""
    text1 = ""
    if type(text) is not str:
         raise TypeError("text must be a string")
    elementos = [".","?",":"]
    for i in text:
        text1 += i
        if i in elementos:
            print(f"{text1.strip()}\n")
            text1 = ""
    print(f"{text1.strip()}",end="")
