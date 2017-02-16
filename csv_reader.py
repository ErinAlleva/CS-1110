# Alex Hicks (awh4kc)

import csv

datafile = open("wendys.csv", "r")

datafile.readline()

list_of_lines = []

for line in datafile:
    split_line = line.strip().split(";")
    list_of_lines.append(split_line)

print(list_of_lines)

data_we_want = []

for line in list_of_lines:
    data_we_want.append(line[1])

print(data_we_want)

