#!/usr/bin/python3

from decimal import Decimal


TAX_RATE = {
    0: Decimal('0.1'),
    10000: Decimal('0.2'),
    50000: Decimal('0.3'),
    100000: Decimal('0.4'),
    500000: Decimal('0.5')
}

def tax_range_find(amount):
    result = 0
    for income, rate in TAX_RATE.items():
        if (amount >= income):
            result = rate
    return result


def tax_caculate(amount):
    if not (isinstance(amount, int) or isinstance(amount, float)):
        raise ValueError('unaccepted input')
    return amount * tax_range_find(amount)

# print(tax_caculate(77000))
