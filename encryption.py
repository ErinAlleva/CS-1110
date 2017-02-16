# Alex Hicks (awh4kc)

plaintext = input("what should we turn into oppish?: ")
plaintext = plaintext.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
ciphertext = ""
for letter in plaintext:
    if letter in vowels:
        ciphertext += "op"

    ciphertext += letter

print(ciphertext)

index = 0
decrypted = ""

while index < len(ciphertext):
    if ciphertext[index] == 'o' and ciphertext[index + 1] == 'p':
        decrypted += ciphertext[index + 2]
        index += 3
    else:
        decrypted += ciphertext[index]
        index += 1

print(decrypted)

