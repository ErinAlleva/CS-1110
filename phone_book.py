# Alex Hicks (awh4kc)

phone_book = {}
reverse_phone_book = {}

for i in range (5):
    new_person = input("Add an entry to the phone book: ").split()
    print(new_person)

    phone_book[new_person[0]] = new_person[1]
    reverse_phone_book[new_person[1]] = new_person[0]

look_up = input("Who do you want to call?: ")

if look_up in phone_book:
    print(look_up + "'s number is: " + phone_book.get(look_up))
else:
    print("That name is not in the phone book.")

look_number = input("Which number do you want to look up?: ")

if look_number in reverse_phone_book:
    print("That number belongs to: " + reverse_phone_book.get(look_number))
else:
    print("That number is not in the phone book.")
