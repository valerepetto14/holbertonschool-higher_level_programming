#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    coinciden = set_1.intersection(set_1, set_2)
    res = (set_1.union(set_1, set_2) - coinciden)
    return res
