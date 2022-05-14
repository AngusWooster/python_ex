#!/usr/bin/python3

import codecs
######################################
#   ord() <-- get ASCII of charcter
#   chr() <--- ASCII to charcter




def rot13(word):
    output = []
    output_str = ''
    for c in word.lower():
        ascii_val = ord(c) + 13 # move charcter to next 13th charcter
        if (ascii_val > ord('z')):
            ascii_val -= 26
        output.append(chr(ascii_val))
        output_str += chr(ascii_val)
    print("output: ",output)
    return output_str #''.join(output)

print("==========================")
print(rot13("apple"))
print(rot13("nccyr"))
print("==========================")
print(codecs.encode("apple", "rot_13"))
print(codecs.encode("nccyr", "rot_13"))