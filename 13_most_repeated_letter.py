#!/usr/bin/python3

from cgi import test
import operator
from typing import Counter
from unittest import result


test_pattern = 'independence'

# def most_repeated_letter(string):
#     letters = list(set(string))
#     letters_count = []

#     for letter in letters:
#         letters_count.append((letter, string.count(letter)))

#     result = sorted(letters_count, key=operator.itemgetter(1))[-1]
#     print(f'{result[0]}, repeat: {result[1]}')

def most_repeated_letter(string):
    letters_count = Counter(string).most_common(1)
    result = letters_count[0]
    print(f'{result[0]}, repeat: {result[1]}')

most_repeated_letter(test_pattern)
# print(set(test_pattern))
