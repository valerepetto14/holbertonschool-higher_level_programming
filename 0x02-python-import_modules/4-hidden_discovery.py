#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    array = dir(hidden_4)
    for iter in array:
        if (iter[0] != '_' and iter[1] != '_'):
            print(f"{iter}")
