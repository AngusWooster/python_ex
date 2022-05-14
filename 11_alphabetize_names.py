#!/usr/bin/python3


import operator


people = [
    ('joe', 'biden', 'people@usa.gov'),
    ('emmanuel', 'macron', 'people@france.gov'),
    ('justin', 'trudeau', 'people@canada.gov'),
    ('angela', 'merkel', 'people@germany.gov'),
    ('jacinda', 'arden', 'people@newzealand.gov'),
]

def last_to_first_sorting(d):
    return (d[1], d[0])

for person in sorted(people, key=last_to_first_sorting):
    print(person)

for person in sorted(people, key=operator.itemgetter(1,0)):
    print(person)