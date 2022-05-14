#!/usr/bin/python3


menu = {
    'apple': 100,
    'milk': 50,
    'cookie': 20
}


def order_meal():
    total = 0
    while True:
        order = input('input which meal you want: ')
        if (order == ''):
            break

        if order in menu:
            price = menu[order]
            total += price
            print(f'total is {total}')
        else:
            print("no this meal")
    print(f'total amount is {total}')

order_meal()