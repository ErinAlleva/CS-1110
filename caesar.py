# Alex Hicks (awh4kc)

alphabet = {'h': 'a', 'i': 'b', 'j': 'c', 'k': 'd',
            'l': 'e', 'm': 'f', 'n': 'g', 'o': 'h',
            'p': 'i', 'q': 'j', 'r': 'k', 's': 'l',
            't': 'm', 'u': 'n', 'v': 'o', 'w': 'p',
            'x': 'q', 'y': 'r', 'z': 's', 'a': 't',
            'b': 'u', 'c': 'v', 'd': 'w', 'e': 'x',
            'f': 'y', 'g': 'z'}

word = list(input("Enter your cipher text: ").lower())

for i in range(len(word)):
    if word[i] in alphabet:
        word[i] = alphabet[word[i]]

print("The decoded phrase is: " + "".join(word))

# print("The decoded phrase is: " + "".join(word))
#
# # Alex Hicks (awh4kc)
#
# alphabet = {'f': 'a', 'g': 'b', 'h': 'c', 'i': 'd',
#             'j': 'e', 'k': 'f', 'l': 'g', 'm': 'h',
#             'n': 'i', 'o': 'j', 'p': 'k', 'q': 'l',
#             'r': 'm', 's': 'n', 't': 'o', 'u': 'p',
#             'v': 'q', 'w': 'r', 'x': 's', 'y': 't',
#             'z': 'u', 'a': 'v', 'b': 'w', 'c': 'x',
#             'd': 'y', 'e': 'z'}
#
# word = list(input("Enter your cipher text: ").lower())
#
# for i in range(len(word)):
#     if word[i] in alphabet:
#         word[i] = alphabet[word[i]]
#
# print("The decoded phrase is: " + "".join(word))
