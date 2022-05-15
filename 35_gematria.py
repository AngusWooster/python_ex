#!/usr/bin/python3


import string


def gematria_dict():

    return {ch:idx
            for idx, ch in enumerate(string.ascii_lowercase, 1)}


# print(gematria_dict())
GEMATRIA_DICT = gematria_dict()

def gematria_value(word):
    out_val = 0
    for ch in word.lower():
        if ch in GEMATRIA_DICT:
            out_val += GEMATRIA_DICT[ch]
    return out_val

print(gematria_value("programming"))
print(gematria_value("professor"))
print(gematria_value("explanation"))

def gemetria_equal_words(input_word, filename):
    input_value = gematria_value(input_word)
    output_words = list()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.lower().split():
                if input_value == gematria_value(word):
                    output_words.append(word)
    return output_words


