#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def remplazar(num):
        if num == search:
            num = replace
        return num
    lista = list(map(remplazar, my_list))
    return lista
