# Alex Hicks (awh4kc)
#

import random
import string
import re


gimme_input = input("Enter your text: ")
seed = (input("Enter a seed (0 for random): "))

if seed != 0:
    random.seed(seed)

answer = []
split = gimme_input.split(" ")

def scramble_word(word):
    if len(split[i]) == 1:
        answer.append((split[i])[0])
    else:
        split2 = list(split[i])
        split1 = list(((split[i])[1:-1]))
        random.shuffle(split1)
        answer.append(((split[i])[0] + "".join(split1) + (split[i])[-1]))

for i in range(0, len(split)):
    scramble_word(gimme_input)

print("Your scrambled sentence is: " + " ".join(answer))

#count from the back
#cut using that counter

