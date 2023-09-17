#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = []
    for i in range(len(str)):
        if i != n:
            newStr.append(str[i])

    return "".join(newStr)
