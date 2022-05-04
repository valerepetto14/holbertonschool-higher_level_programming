#!/usr/bin/python3
def weight_average(my_list=[]):
    if(len(my_list) == 0):
        return 0
    suma = 0
    divisor = 0
    for i in my_list:
        suma += i[0] * i[1]

    for i in my_list:
        divisor += i[1]

    return suma / divisor
