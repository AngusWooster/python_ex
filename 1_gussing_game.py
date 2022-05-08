#!/usr/bin/python3
import random


def guessing_game():
    ans = random.randint(0, 100)
    print ("guessing game ans: %d" %(ans))
    while True:
        num = input("input val: ")

        if (not num.replace('.','').isdigit()):
            print ("please input integrate")
            continue

        num = int(float(num))

        if (num == ans):
            print ("You got it, Congratulation")
            break
        elif (num > ans):
            print ("Your value is bigger than ANS")
        else:
            print ("Your value is smaller than ANS")


guessing_game()