#!/usr/bin/python3
def element_at(my_list, idx):
    lenlist = len(my_list)
    elif(idx < 0):
        return None
    elif (idx >= lenlist):
        return None
    else:
        return (my_list[idx])
