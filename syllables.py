# Alex Hicks (awh4kc)

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'aa', 'ae', 'ai',
          'ao', 'au', 'ay', 'ea', 'ee', 'ei', 'eo', 'eu',
          'ey', 'ia', 'ie', 'ii', 'io', 'iu', 'iy', 'oa',
          'oe', 'oi', 'oo', 'ou', ',oy', 'ya', 'ye', 'yi',
          'yo', 'yu', 'yy']
not_vowels = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
             'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
             'x', 'z']

word = input("Please give me a word: ").lower()
word_list = list(word)
number_of_vowels = int()
number_of_not_vowels = int()

for i in range(0, len(word)):
    if word[i] in vowels and word[i-1] not in vowels:
        number_of_vowels += 1
    if word[i] in vowels and word[i - 1] in vowels:
        number_of_vowels += 0
    elif word[i] in not_vowels:
        number_of_not_vowels += 1

if len(word) == 1 and word in vowels:
    number_of_vowels = 1

print(number_of_vowels)
print(number_of_not_vowels)

if number_of_vowels == 0:
    number_of_vowels == 1
elif word_list[len(word)-1] == "e":
    if number_of_vowels != 1:
        number_of_vowels -= 1
    else:
        number_of_vowels == 1

number_of_vowels = str(number_of_vowels)

print("The word " + word + " has " + number_of_vowels + " syllables.")

