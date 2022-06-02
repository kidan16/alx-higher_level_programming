#!/usr/bin/python3
from sys import argv
if len(argv) == 1:
    separetor = "."
else:
    separetor = ":"
if __name__ == "__main__":
    print("{} arguments{}".format(len(argv), separetor))
    if len(argv) > 1:
        for i in range(1, len(argv) + 1):
            print("{}: {}".format(i, argv[i]))
