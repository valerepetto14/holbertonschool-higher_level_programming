#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)
    if(lenA < 2):
        while lenA < 2:
            tuple_a = tuple_a + (0, )
            lenA += 1
    if (lenB < 2):
        while lenB < 2:
            tuple_b = tuple_b + (0, )
            lenB += 1

    new_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return (new_tuple)
