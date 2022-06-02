#!/usr/bin/python3
from sys import argv
length = len(argv)
i = 1
if length < 2:
    separetor = "."
else:
    separetor = ":"
if __name__ == "__main__":
    print("{} arguments{}".format(length, separetor))
    if length > 1:
        for i in range(1, length + 1):
            print("{}: {}".format(i, argv[i]))
    else:
        print("")
