# Alex Hicks (awh4kc)
# I talked things over with my friend Andrew (abw3yd)
# I found the import re on https://docs.python.org/3/library/re.html

import random, string, re

gimme_input = input("Enter your text: ")
seed = int(input("Enter a seed (0 for random): "))

if seed != 0:
    random.seed(seed)

def scramble_word(word):

    slice_and_dice = re.compile(r'\s')
    split_stuff = slice_and_dice.split("".join(letter for letter in word if letter not in set(string.punctuation)))
    for split in split_stuff:
        if len(split) < 4:
            continue
        else:
            mixed_up = list(split[1:-1])
            random.shuffle(mixed_up)
            scrambled = (split[0], "".join(mixed_up), split[-1])
            scrambled = "".join(scrambled)
        word = word.replace(split, scrambled, 1)

    return word

print("Your scrambled sentence is : " + scramble_word(gimme_input))

