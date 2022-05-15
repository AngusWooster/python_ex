#!/usr/bin/python3


def flatten(data_sets):
    elements = []
    for set in data_sets:
        for element in set:
            elements.append(element)
    return elements

print(flatten([[1,2],[3,4]]))