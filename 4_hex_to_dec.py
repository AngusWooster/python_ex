#!/usr/bin/python3

def hex_to_dec():
    str = input("input a hex value(exclude prefix '0x'): ")
    print("dec: ",int(str, 16))

def hex_to_dec2():
    val = 0
    digit_num = 0
    str = input("input a hex value(exclude prefix '0x'): ")
    str = str.upper()
    print(str)

    for power, digit in enumerate(reversed(str)):
        print("power = ",power," CH: ", digit, "ASCII: ", ord(digit))

        if (digit.isdigit()):
            digit_num = int(digit)
        else:
            digit_num = ord(digit) - ord("A") + 10
        val += digit_num * (16**power)
    print("dec: ",val)

hex_to_dec()