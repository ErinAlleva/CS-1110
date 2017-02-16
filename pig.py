# Alex Hicks (awh4kc)
# Kevin Dela Merced (krd5sv)

import random

player_score = 0
computer_score = 0
player_temp = 0
computer_temp = 0

while computer_score < 50 and player_score < 50:
    keep_rolling = 'x'
    computer_rolling ='x'
    while keep_rolling is 'x':
        print("Player: " + str(player_score) + " Computer: " + str(computer_score))
        print("It's your turn!")
        roll = random.randint(1,6)
        if roll is 1:
            print("You rolled a " + str(roll))
            print("PIG! Too bad! Your total is currently:" + str(player_score))
            player_temp = 0
            print()
            break
        else :
            print("You rolled a " + str(roll))
            player_temp = player_temp + roll
            print("You currently have " + str(player_temp) + " banked.")
            roll_again = input("Do you wish to roll again (y/n)?:")
            if roll_again == 'n':
                keep_rolling = 'y'
                player_score += player_temp
                print("Your total score is now: " + str(player_score))
                player_temp = 0
        if player_score >= 50:
            print("The player wins!" + str(player_score) + "to" + str(computer_score))
            break

    while computer_rolling is 'x' and player_score < 50:
        print("Player: " + str(player_score) + " Computer: "+ str(computer_score))
        print("It's the computer's turn!")
        c_roll = random.randint(1,6)
        if c_roll is 1:
            print("The computer rolled a ", str(c_roll))
            print("PIG! Too bad! The computer's total is currently: " + str(computer_score))
            computer_temp = 0
            print()
            break
        print("The computer rolled a " + str(c_roll))
        computer_temp = computer_temp + c_roll
        print("The computer has "+  str(computer_temp) + " banked.")
        if computer_temp >= 10:
            computer_rolling = 'n'
            print("The computer has chosen to end its turn.")
            computer_score += computer_temp
            computer_temp = 0
            print("Computer' score is now:" + str(computer_score))
        if computer_score >= 50:
            print("The computer wins!" + str(computer_score) + " to " + str(player_score))
            break

