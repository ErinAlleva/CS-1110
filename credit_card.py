# Alex Hicks (awh4kc)

cc_number = input("Type a credit card number (just digits): ")
cc_number_list = list(cc_number)
even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
list_of_rightmost = []

for i in range(len(cc_number_list), 0, -2):
    if len(cc_number_list) % 2 in even:
        i = int(i) + 1
        list_of_rightmost.append(cc_number_list[i-2])
    elif len(cc_number_list) % 2 in odd:
        i = int(i)
        list_of_rightmost.append(cc_number_list[i-1])

list_of_rightmost1 = [int(i) for i in list_of_rightmost]
total = sum(list_of_rightmost1)

list_of_remaining = []
for i in range(len(cc_number_list) - 1, 0, -2):
    if len(cc_number_list) % 2 in even:
        i = int(i) + 1
        list_of_remaining.append(cc_number_list[i-2])
    elif len(cc_number_list) % 2 in odd:
        i = int(i)
        list_of_remaining.append(cc_number_list[i-1])

list_of_remaining1 = [2 * int(i) for i in list_of_remaining]
sum_thing = "".join(map(str, list_of_remaining1))
sum_thing1 = list(sum_thing)
sum_thing2 = [int(i) for i in sum_thing1]

total2 = sum(sum_thing2)

grand_total = total + total2

if grand_total % 10 == 0:
    print("Yes, " + cc_number + " is a valid credit card number")
else:
    print(cc_number + " is not a valid credit card number")

