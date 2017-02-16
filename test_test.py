# Alex Hicks (awh4kc)

datafile = open("births", "r")
datafile.readline

for line in datafile:
    decoded = line.strip().split(",")

monday = 0
tuesday = 0
wednesday = 0
thursday = 0
friday = 0
saturday = 0
sunday = 0
for i in range(len(decoded[3])):
    if decoded[3][i] == 0:
        monday += int(decoded[4][i])
    elif decoded[3][i] == 1:
        monday += int(decoded[4][i])
    elif decoded[3][i] == 2:
        monday += int(decoded[4][i])
    elif decoded[3][i] == 3:
        monday += int(decoded[4][i])
    elif decoded[3][i] == 4:
        monday += int(decoded[4][i])
    elif decoded[3][i] == 5:
        monday += int(decoded[4][i])
    elif decoded[3][i] == 6:
        monday += int(decoded[4][i])
list = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
max_thing = max(list)
index_thing = list.index(max_thing)
real_index = decoded[3].index(index_thing)
if real_index == 0:
    print("Monday", max_thing)
elif real_index == 1:
    print("Tuesday", max_thing)
elif real_index == 2:
    print("Wednesday", max_thing)
elif real_index == 3:
    print("Thursday", max_thing)
elif real_index == 4:
    print("Friday", max_thing)
elif real_index == 5:
    print("Saturday", max_thing)
else:
    print("Sunday", max_thing)
