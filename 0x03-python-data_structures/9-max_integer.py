#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        mayor = my_list[0]
        for i in range(len(my_list)):
            if(my_list[i] > mayor):
                mayor = my_list[i]
        return mayor
    else:
        return None
