#!/usr/bin/python3

from curses.ascii import isdigit


def record_rainfall():
    rain_fall = {} # (): tuple, []: list, {}: dict
    while True:
        city = input("input city: ")

        if (city == ''):
            break
        rain_mm = input('input rain(mm): ')
        if (rain_mm.isdigit() == False):
            rain_mm = 0

        rain_fall[city] = rain_fall.get(city, 0) + int(rain_mm)


    for record in rain_fall.items():
        print('city: {0:20s}/{1} mm'.format(*record))


record_rainfall()