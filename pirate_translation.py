# Alex Hicks (awh4kc)

word = input("What word do you want to translate: ")

pirate_dictionary = {'hello' : 'yarr', 'friend' : 'matey',
                'hi' : 'ahoy'}

print("The translation is:",
      pirate_dictionary.get(word.lower(), "not here!"))
