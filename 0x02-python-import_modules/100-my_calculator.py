#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    res = 0
    if((len(sys.argv) - 1) != 3):
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if(sys.argv[2] == "+"):
            print(f"{a} + {b} = {add(a, b)}")
        elif(sys.argv[2] == "-"):
            print(f"{a} - {b} = {sub(a, b)}")
        elif(sys.argv[2] == "*"):
            print(f"{a} * {b} = {mult(a, b)}")
        elif(sys.argv[2] == "/"):
            print(f"{a} / {b} = {div(a, b)}")
        else:
            print(f"Unknown operator. Available operators: +, -, * and /")
            exit(1)
