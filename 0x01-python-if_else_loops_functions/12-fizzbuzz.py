#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if((a % 3) == 0 and (a % 5) == 0):
            print(f"FizzBuzz ", end="")
        elif((a % 3) == 0):
            print(f"Fizz ", end="")
        elif((a % 5) == 0):
            print(f"Buzz ", end="")
        else:
            print(f"{a} ", end="")
        if(a == 100):
            continue
        print("", end="")
    return (0)
