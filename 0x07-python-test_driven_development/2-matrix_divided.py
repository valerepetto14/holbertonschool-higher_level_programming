#!/usr/bin/python3
"""
function matrix devided 
"""

def matrix_divided(matrix, div):
    """def matrix"""
    result = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None:
        raise TypeError("matrix_divided() missing 1 required positional argument: 'div'")
    if(matrix == []):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for i in matrix:
        if(len(i) == 0):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:##recorro para saber si no tienen enteros o floats
        for a in range(len(i)):
            if(type(i[a]) is not int and type(i[a]) is not float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")        
    for e in range(len(matrix)):
        if e == len(matrix) - 1:
            continue;
        if (len(matrix[e]) != len(matrix[e + 1])):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            continue
    for lista in matrix :
        newmatrix = []
        for num in lista:
            newmatrix.append(round((num / div),2))
        result.append(newmatrix)
    return result