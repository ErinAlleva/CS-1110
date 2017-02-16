import random
import string
import re

gimme_input = input("Enter your text: ")
seed = int(input("Enter a seed (0 for random): "))

if seed != 0:
    random.seed(seed)

def scramble_word(word):

    slice_and_dice = re.compile(r'\s')
    split_stuff = slice_and_dice.split(u''.join(punctuation for punctuation in word if punctuation not in set(string.punctuation)))
    scrambled = []
    for split in split_stuff:
        if len(split) < 4:
            continue
        else:
            mid = list(split[1:-1])
            random.shuffle(mid)
            scrambled = (split[0], "".join(mid), split[-1])
            scrambled = "".join(scrambled)
        word = word.replace(split, scrambled, 1)

    return word

print("Your scrambled sentence is : " + scramble_word(gimme_input))

