# Alex Hicks (awh4kc)

print(5//8)

my_list = ['things', 'things2', 'things3']

for thing in my_list:
    print(thing)

for i in range(len(my_list)):
    print(my_list[i])

string = "This is a string to read."

print(string.split())

my_dictionary = {}

my_dictionary["key"] = "value"
print(my_dictionary)
# .get(), .append(), in

for i in range(5):
    for j in range(5):
        print(i*j)

# '' or "" are the same

string_number = "4"
number_of_string_number = int(string_number)

x = 5

x = x + 1
x += 1

#mutable - str, int, bool, float - does not change
#immutable (reference) - list, set, dict - two parts,
# a pointer to a location where the data is stored

title = "CS1110IntroToProgramming"
print(title.index('1110'))
print(title.index('o'))
#searches and gives the location of the string in title

print(26%5)

#syntax - won't run, imporper grammar, etc
#logical - doing the wrong thing - no error onscreen
#runtime - program executes but fails, divide by 0

#dictionaries are unordered and list are ordered

my_list2 = my_list.copy()

import random

print(random.randint(1,6))

#random.randint(inclusive, inclusive)
#range(inclusive, exclusive)

#True or False
done = False
while not done:
    done = True

#while loop - dont know when it will run
#for loop - know when it will run