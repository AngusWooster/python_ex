#!/usr/bin/python3

numbers = [1,2,3,1,2,3,4,1,2]

def unique_num_len(numbers):
    return len(set(numbers))


print(unique_num_len(numbers))