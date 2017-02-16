# Alex Hicks (awh4kc)

datafile = open("thanksgiving.csv", "r")

datafile.readline()

count_turkey = 0
count_responses = 0

for line in datafile:
    decoded = line.strip().split(";")

    if "Turkey" in decoded[2] and "Yes" == decoded[1]:
        count_turkey += 1
    count_responses += 1

print(count_turkey, "/", count_responses)

