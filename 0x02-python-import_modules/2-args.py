#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        separetor = "."
    else:
        separetor = ":"
    print("{} arguments{}".format(len(argv) - 1, separetor))
    if len(argv) > 1:
       for i in range(1, len(argv)):
            print('{}: {}'.format(i, argv[i]))
