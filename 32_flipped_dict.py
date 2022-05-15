#!/usr/bin/python3

from curses import keyname


TEST_DICT = {'a':1, 'b':2, 'c':3}

def flipped_dict1(input_dict):
    output_dict = {}
    for key in input_dict:
        # output_dict.append(key, input_dict[key])
        output_dict[input_dict[key]] = key
    return output_dict

def flipped_dict2(input_dict):
    return {input_dict[key]:key
            for key in input_dict}

print(flipped_dict1(TEST_DICT))
print(flipped_dict2(TEST_DICT))


