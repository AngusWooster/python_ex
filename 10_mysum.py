#!/usr/bin/python3


def mysum(*items):
    if not items:
        return items
    output = items[0]

    for item in items[1:]:
        if (isinstance(item, dict)):
            output |= item
        else:
            output += item
    return output


print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum('abc', 'd', 'e'))
print(mysum([10, 20, 30], [40, 50], [60]))
print(mysum({'x':1, 'y':2},{'z':3}))



d1 = {'a':1, 'b':2}
d2 = {'c':3}
print(d1 | d2)