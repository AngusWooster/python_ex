#!/usr/bin/python3

def pig_latin(word):
    if (word[0] in 'aeiou'):
        return f"{word}way"
        #return word + "way"
    else:
        return f"{word[1:]}{word[0]}ay"
        #return word[1:] + word[0] + "ay"

    

print(pig_latin('air'))         # expected output: airway
print(pig_latin('eat'))         # expected output: airway
print(pig_latin('python'))      # expected output: ythonpay
print(pig_latin('computer'))    # expected output: omputercay

# additional exercise
## different id which means different object
word = 'python'
print(id(word))
word = word + "abc"
print(id(word))