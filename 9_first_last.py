#!/usr/bin/python3

def first_last(seq):
    return seq[:1] + seq[-1:]

print(first_last('abcde'))
print(first_last([1,2,3,4,5]))