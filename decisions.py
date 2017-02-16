# Alex Hicks (awh4kc)

cold_threshold = int(input("What is your cold threshold? "))
current_temp = int(input("What is the current temp? "))
is_cold = False
pants_day = False

if current_temp < cold_threshold:
    is_cold = True

if is_cold and pants_day:
    print("Wear coat")
    print("Wear scarf")
    print("Wear pants")

if is_cold:
    print("Wear pants")
else:
    print("Who needs pants?")

if is_cold:
    print("Wear more pants")
elif pants_day:
    print("Must wear pants on pants day!")
elif 1 == 1:
    print("Yup, that's 1 == 1...")
else:
    print("Who needs pants?")

# < > - less than, greater than
# <= >= - less than or equal to, greater than or equal to
# == - checking for equality
# not - negates a thing
# or - one or the other
# and - both must be true

dictionary = {"hello":"Yarrr!!"}

word = input("What word would you like translated?: ")

pirate_dictionary = {"hello" : "Yarr", "hi" : "ahoy"}

word_to_add = input("Give me a word and translation to add: ").split()

if word_to_add[0] in pirate_dictionary:
    print("That is already here")
else:
    pirate_dictionary[word_to_add[0]] = word_to_add[1]

if word.lower() in pirate_dictionary:
    print("The translation is:", pirate_dictionary.get(word.lower(), "Not here!"))
else:
    print("I cannot translate that...")
