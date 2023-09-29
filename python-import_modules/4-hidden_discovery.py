#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    listH = [c for c in dir(hidden_4) if c[0] != '_']
    listH.sort()

    for i in listH:
        print(i)
