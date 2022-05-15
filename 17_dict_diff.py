#!/usr/bin/python3


d1 = {'a':1, 'b':2, 'c':2, 'd':5}
d2 = {'a':1, 'b':3, 'd':4, 'e':6}

def dict_diff(first, second):
    output = {}
    all_keys = sorted(d1.keys() | d2.keys())

    for key in all_keys:
        if (first.get(key) != second.get(key)):
            output[key] = [first.get(key), second.get(key)]
    return output


print(dict_diff(d1, d2))