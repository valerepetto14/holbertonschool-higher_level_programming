#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    if roman_string == "":
        return 0
    suma = 0
    dic_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman_string)):
        if i > 0 and dic_val[roman_string[i]] > dic_val[roman_string[i - 1]]:
            suma += dic_val[roman_string[i]] - 2 * dic_val[roman_string[i - 1]]
        else:
            suma += dic_val[roman_string[i]]
    return suma
