#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    ls = len(argv)
    r = 0

    if ls != 1:
        for i in range(1, ls):
            r += int(argv[i])
    print("{0}".format(r))
