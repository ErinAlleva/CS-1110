# Alex Hicks (awh4kc)

def cville_weather(filename):

    datafile = open("cville_weather_sept15.csv", "r")

    datafile.readline()

    list_of_temps = []

    for line in datafile:
        split_line = line.strip().split(",")
        list_of_temps.append(int(split_line[1]))

    return sum(list_of_temps) / len(list_of_temps)

print(cville_weather("cville_weather_sept15.csv"))

