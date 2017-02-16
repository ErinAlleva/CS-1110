# Alex Hicks (awh4kc)
# Elizabeth Zhang (ez9pw)

import math
import webbrowser
datafile = open("wendys.csv", "r")

datafile.readline()

list_of_lines = []

for line in datafile:
    split_line = line.strip().split(";")
    list_of_lines.append(split_line)

user_lat = float(input("What is your latitude? "))
user_lon = float(input("What is your longitude? "))

def distance_between(lat_1, lon_1, lat_2, lon_2):
    theta = lon_1 - lon_2
    dist = math.sin(lat_1 * math.pi / 180.0) * math.sin(lat_2 * math.pi / 180.0) + math.cos(lat_1 * math.pi / 180.0) * math.cos(lat_2 * math.pi / 180.0) * math.cos(theta * math.pi / 180.0)
    dist = math.acos(dist)
    dist = dist * 180.0 / math.pi
    dist = dist * 60 * 1.1515

    return dist

list_of_distances = []

for i in range(len(list_of_lines)):
    wendys_lat = float(list_of_lines[i][0])
    wendys_lon = float(list_of_lines[i][1])
    distance = distance_between(user_lat, user_lon, wendys_lat, wendys_lon)
    list_of_distances.append(distance)

correct = min(list_of_distances)

index_thing = list_of_distances.index(correct)

string_thing = str((list_of_lines[index_thing][4]) + (list_of_lines[index_thing][5] + (list_of_lines[index_thing][6])))

url = "http://maps.google.com/maps?q=" + string_thing

url = url.replace(' ', '+')

webbrowser.open(url)

