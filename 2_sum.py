#!/usr/bin/python3

def my_sum(*args, start = 0):
    '''
    print(args)
    print(type(args))
    '''
    output = 0
    for n in args:
        #print("n = %d" %n)
        output += n
    return output + start

print ("output = %d" %my_sum(1, 2, 3, 4, 5))
print ("output = %d" %my_sum(1, 2, 3, 4, 5, start = 10))