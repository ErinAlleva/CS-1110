# Alex Hicks (awh4kc)

phonebook = {'Alex' : '540-336-1860', 'Amanda' : '434-243-2313',
             'Sammy' : '434-234-2343'}

gradebook = {'mss2x':[99,98,80], 'tbh3f':[89,90,78], 'asb2t':[70,66,73]}

print(gradebook)
print(gradebook['mss2x'])

print('mss2x' in gradebook)
print('lat7h' in gradebook)

# user_to_check = input("Get average for student: ")
# test_average = sum(gradebook[user_to_check])/len(gradebook[user_to_check])
# print(test_average)

employee = {'compid' : 'mss2x', 'name' : 'Mark Sherriff',
            'dob' : '11/09/79', 'year':10, 'room':401}

employees = {}
employees.append(employee)
employees.append({'compid' : 'tbh3f', 'name' : 'Tom Horton',
                  'dob' : '08/09/59', 'year' : 'forever', 'room' : 402})

print(employees)

# clear() - empties the dict
# get() - gets a particular value based on key
# items() - gets all the keys and values
# keys() - gets all the available keys
# pop(key) - gets a value, and deletes the key/value pair
# values() - gets all the values

print(gradebook)
print(gradebook.pop('mss3x'))
print(gradebook)
print(gradebook.get('mss2x', 'Not in here!'))
print(gradebook.get('tbh3f', 'Not in here!'))

