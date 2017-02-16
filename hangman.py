# Alex Hicks (awh4kc)
# I talked over ideas with my friend Andrew (abw9yd)

word = input("Enter a word: ").upper()
dash_word = "-" * len(word)
dash_word_list = list(dash_word)

count = 6
finished = False

while not finished:
    print("[" + "".join(dash_word_list) + "]")
    guess_letter = input("You have " + str(count) + " left, enter a letter: ").upper()
    if guess_letter in word:
        for i in range(0, len(word)):
            if word[i] == guess_letter:
                dash_word_list[i] = word[i]
        if "-" in dash_word_list:
            print("Correct!")

    else:
        count -= 1
        if count == 0:
            print('You lose! The word was "' + "".join(word) + '"')
            finished = True
        if "-" not in word and count != 0:
            print("Incorrect!")

    if "-" not in dash_word_list:
        print('You win! The word was "' + "".join(word) + '"')
        finished = True

