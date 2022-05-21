#!/usr/bin/python3
"""
function matrix devided 
"""

def matrix_divided(matrix, div):
    """def matrix"""
    result = []
    #if(matrix is None):
        #raise TypeError("TypeError: matrix_divided() missing 1 required positional argument: 'div'")
    #if (type(matrix) is not list and type(div) is not int):
        #raise ValueError("matrix or div is not a possible value")
    if matrix is None:
        raise TypeError("matrix_divided() missing 1 required positional argument: 'div'")
    if (type(matrix) is int):
        raise TypeError("'int' object is not iterable")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        for a in i:
            if(type(a) is not int and type(a) is not float):
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