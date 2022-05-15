#!/usr/bin/python3


def passwd_to_dict(filename):
    output = {}
    with open(filename) as f:
        for line in f:
            info = line.split(':')
            output.update({info[0]:info[2]})
    return output

print(passwd_to_dict("/etc/passwd"))