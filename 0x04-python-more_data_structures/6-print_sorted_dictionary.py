#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in a_dictionary.keys():
        print(f"{i} : {a_dictionary.get(i)}")
