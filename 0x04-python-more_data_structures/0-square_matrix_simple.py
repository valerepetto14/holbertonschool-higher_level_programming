#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square(lista):
        listasquar = list(map(lambda x: x * x, lista))
        return (listasquar)
    lista = list(map(square, matrix))
    return (lista)
