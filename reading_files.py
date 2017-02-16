# Alex Hicks (awh4kc)

def fav_cartoon(filename):

    datafile = open("new_friends.txt", "r")

    cartoon_dict = {}

    datafile.readline()

    for line in datafile:
        print(line.strip().split(","))
        split_line = line.strip().split(",")
        if split_line[1] in cartoon_dict:
            cartoon_dict[split_line[1]] += 1
        else:
            cartoon_dict[split_line[1]] = 1
    return cartoon_dict

print(fav_cartoon("new_friends.txt"))

