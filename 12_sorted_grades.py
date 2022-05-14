#!/usr/bin/python3

import operator


grades = [
    ('alice', 'wooding', 89),
    ('bob', 'johnson', 86),
    ('cindy', 'letterman', 93),
    ('david', 'moor', 86),
    ('eddie', 'williams', 91),
]

def sorted_grades(grades):
    output = []
    for first, last, grade in sorted(grades, key=operator.itemgetter(2), reverse=True): # reverse=True: ordering from big to small
        # print(f'{first:20s}{last:20s}{grade}')
        # output.append(f'{first:20s}{last:20s}{grade}')
        output.append('{0:20s}{1:20s}{2:5.1f}'.format(first, last, grade))
    return '\n'.join(output)

print(sorted_grades(grades))