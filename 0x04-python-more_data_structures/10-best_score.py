#!/usr/bin/python3
def best_score(a_dictionary):
    mayor = 0
    key_mayor = ""
    if a_dictionary is ZZNone:
        return None
    for i in a_dictionary:
        if a_dictionary[i] > mayor:
            mayor = a_dictionary[i]
            key_mayor = i
    if mayor == 0:
        return None
    return key_mayor
