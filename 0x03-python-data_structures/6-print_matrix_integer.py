#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    lenlist = len(matrix)
    i = 0
    while (i < lenlist):
        len_pos = len(matrix[i])
        a = 0
        while(a < len_pos):
            print(f"{matrix[i][a]}", end="")
            if(a < len_pos - 1):
                print(" ", end="")
            a += 1
        print("")
        i += 1
