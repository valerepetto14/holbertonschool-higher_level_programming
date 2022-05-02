#!/usr/bin/python3
def element_at(my_list, idx):
    lista = []
    lenlist = len(my_list)
    if type(lista) != type(my_list):
        return None
    elif(idx < 0):
        return None
    elif (idx > lenlist):
        return None
    else:
        return (my_list[idx])
