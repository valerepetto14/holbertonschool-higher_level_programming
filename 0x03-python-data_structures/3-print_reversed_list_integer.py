def print_reversed_list_integer(my_list=[]):
    lentlist = len(my_list)
    lentlist -= 1
    while (lentlist >= 0):
        print(f"{my_list[lentlist]}")
        lentlist -= 1
