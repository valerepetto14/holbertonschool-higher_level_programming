#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    suma = 0
    for iter in range(1, len(sys.argv)):
        suma += int(sys.argv[iter])

    print(f"{suma}")
