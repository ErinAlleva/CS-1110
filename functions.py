# Alex Hicks (awh4kc)

# bubba -> "starify" -> b*u*b*b*a

# def starify_word(word):
#     new_word = ""
#     for i in (word):
#         new_word += i + "*"
#
#     return new_word[:-1]
#
# word_to_starify = input("Gimme: ")
#
# print(starify_word(word_to_starify))

my_list = ['a', 'b', 'c', 'd']
my_value = 11

def change_a_value(some_value):
    print("Inside change_a_value()")
    print("   some_value starts as:", some_value)
    some_value *=2
    print("   some_value now is:", some_value)
#    return some_value

def change_a_ref(some_list):
    print("Inside change_a_ref()")
    print("   some_list starts as:", some_list)
    some_list.append('x')
    print("   some_list now is:", some_list)

print("Starting the program!")
print("my_list starts as:", my_list)
change_a_ref(my_list)
print("my_list now is:", my_list)
print("my_value starts as:", my_value)
change_a_value(my_value)
#my_value = change_a_value(my_value)
print("my_value now is still:", my_value)

