# Alex Hicks (awh4kc)

email_1 = "awh4kc@virginia.edu"
email_2 = "ahicks@mvgshome.org"
email_3 = "jedialex27@gmail.com"
email_4 = "jedialex27@comcast.net"

email_addresses = ("awh4kc@virginia.edu", "ahicks@mvgshome.org", "jedialex27@gmail.com", "jedialex27@comcast.net")

animals = ['cow', 'horse', 'sheep', 'dog', 'chicken', 'llama'] # make a new list!

print(animals[0])
print(animals[1])
print(animals[0] == 'cow')
print(animals[0] is 'cow')
print(animals[-1])
print(animals[-2])

print("The " + animals[3] + " and the " + animals[4] + " both sleep in the barn.")

list_of_lists = [["cow", "horse"], [5,6,7,8]]
print(list_of_lists)

print(list_of_lists[0])
print(list_of_lists[0][0])
print(type(list_of_lists[0]))
print(type(list_of_lists[0][0]))

print(animals[2:4])
print(animals[0:-1])
print(animals[:-1])
print(animals[3:])
print(animals[0:len(animals)-1])

letters = ['A', 'B', 'C']
numbers = [1,2,3]
both = letters + numbers
print(both)
print(letters * 3)

del animals[3]
print(animals)
#animals.remove('cow')
print(animals)
print('dog' in animals)
print('cow' in animals)

print(animals.index('cow'))
animals.append('duck')
animals.insert(2, 'pig')
print(animals)
animals.sort()
print(animals)
animals.reverse()
print(animals)

animals2 = animals
print(animals)
print(animals2)
animals.append('unicorn')
print(animals)
print(animals2)

import copy
animals3 = copy.copy(animals)
animals3.append('farmer')
print(animals)
print(animals3)
