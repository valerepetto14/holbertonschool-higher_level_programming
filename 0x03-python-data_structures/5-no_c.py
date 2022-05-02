#!/usr/bin/python3
def no_c(my_string):
    new_string1 = my_string.translate({ord('c'): None})
    new_string2 = new_string1.translate({ord('C'): None})
    return (new_string2)
