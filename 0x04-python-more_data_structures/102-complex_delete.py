#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copia = a_dictionary.copy()
    for i in copia:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
