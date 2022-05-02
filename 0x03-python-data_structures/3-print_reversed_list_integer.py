#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lentlist = len(my_list)
    lentlist -= 1
    lista = []
    if type(lista) == type(my_list):
        while (lentlist >= 0):
            print(f"{my_list[lentlist]:d}")
            lentlist -= 1
