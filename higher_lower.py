# Alex Hicks (awh4kc)

import random

answer = int(input("What should the answer be? "))

win = False

if answer == -1:
    random_number = random.randint(1, 100)
else:
    random_number = answer

for i in range(5):

    if random_number == answer:
        guess = int(input("Guess a number: "))
        if guess < answer:
            print("The number is higher than that.")
        elif guess > answer:
            print("The number is lower than that.")
        elif guess == answer:
            win = True
            print("You win!")
            break

    elif answer == -1:
        guess = int(input("Guess a number: "))
        if guess < random_number:
            print("The number is higher than that.")
        elif guess > random_number:
            print("The number is lower than that.")
        elif guess == random_number:
            win = True
            print("You win!")
            break

if answer == -1 and win == False:
    print("You lose; the number was " + str(random_number))
elif answer != -1 and win == False:
    print("You lose; the number was " + str(answer))
