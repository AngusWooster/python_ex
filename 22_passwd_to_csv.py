#!/usr/bin/python3
import os
import csv

filename = '22_passwd.log.txt'
with open('/etc/passwd', 'r') as frd, (open(filename, 'w', newline='')) as fwr:
    csv_reader = csv.reader(frd, delimiter=':')
    csv_write = csv.writer(fwr, delimiter='\t', lineterminator='\n')

    for line in csv_reader:
        csv_write.writerow([line[0], line[2]])

# os.remove(filename)
