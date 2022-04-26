#!/usr/bin/python3
for i in range(0, 10):
    for a in range(i, 10):
        if (i != a):
            if(i == 8 and a == 9):
                print(f"{i}{a}")
            elif(i != 8 or a != 9):
                print(f"{i}{a}", end=", ")
