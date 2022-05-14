#!/usr/bin/python3

def pig_latin_str_translator(str):
    list_buf = []
    for word in str.lower().split():
        #print("word: ", word)
        if (word[0] in "aeiou"):
            list_buf.append(f"{word}way")
        else:
            list_buf.append(f"{word[1:]}{word[0]}ay")
    print("list: ",list_buf)
    return " ".join(list_buf)

########################################    
#   test pattern: "this is a test"
#   expected output: "histay isway away esttay"
#
print(pig_latin_str_translator('this is a test'))         # expected output: airway
