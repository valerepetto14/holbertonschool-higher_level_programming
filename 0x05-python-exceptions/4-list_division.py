#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    num = []
    for i in range(list_length):
        try:
            c = my_list_1[i] / my_list_2[i]
        except(TypeError):
            c = 0
            print("wrong type")
        except(ZeroDivisionError):
            c = 0
            print("division by 0")
        except(IndexError):
            c = 0
            print("out of range")
        finally:
            num.append(c)
    return num
