#!/usr/bin/python3

def strsort(string):

    print(sorted(string, key=str.lower))
    return ''.join(sorted(string, key=str.lower))

print(strsort("bdxyCma"))