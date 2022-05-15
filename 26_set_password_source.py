#!/usr/bin/python3
import random

def set_password_source(source):
    def password_gen(len):
        output = []
        for i in range(len):
            output.append(random.choice(source))
        return ''.join(output)
    return password_gen

my_password_gen = set_password_source('0123456789abcdefg')
print(my_password_gen(10))