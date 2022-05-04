#!/usr/bin/python3
def roman_to_int(roman_string):
    signos = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    key = signos.keys()
    res = 0
    iterador = 0
    for i in range (len(roman_string)):
        if i == 0:
            res += signos[roman_string[i]]
        else:
            if 
            return res
