#!/usr/bin/python3


def read_final_line(filename):
    with open(filename, 'r') as f:
        for line in f:
            pass

    return line



print(read_final_line('/var/log/syslog'))