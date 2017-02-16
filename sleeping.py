# Alex Hicks (awh4kc)

import urllib.request

def married_analysis():
    datafile = open("sleeping.csv", "r")

    married_breakdown = {}

    for line in datafile:
        split_line = line.strip().split(";")

        if split_line[2] == "Married":
            if split_line[4] in married_breakdown:
                married_breakdown[split_line[4]] += 1
            else:
                married_breakdown[split_line[4]] = 1

    return married_breakdown
