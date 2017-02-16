# Alex Hicks (awh4kc)

import random

state_chances_for_trump = [.238, .569, .304, .324, .634]
electoral_votes_by_state = [13, 29, 20, 9, 18]

trials = int(input("How many simulation runs?: "))
seed = int(input("Enter a seed (0 for random): "))
if seed != 0:
    random.seed(seed)

clinton_score = []
trump_score = []
total = 0
for i in range(trials):

    for j in range(len(electoral_votes_by_state)):
        states = random.random()
        if states < state_chances_for_trump[j]:
            trump_score.append(electoral_votes_by_state[j])
            something = False
        else:
            clinton_score.append(electoral_votes_by_state[j])
            something = True
        clinton_score1 = sum(clinton_score)
        trump_score1 = sum(trump_score)
    if clinton_score1 > trump_score1:
        total += 1
        print("Run " + str(i) + ": Clinton wins with " + str(clinton_score1))
    else:
        print("Run " + str(i) + ": Trump wins with " + str(trump_score1))
    clinton_score = []
    trump_score = []

if trials > 99:
    clinton_win = float(total / trials)
    trump_win = float(1 - clinton_win)
    clinton_win = format(clinton_win, ".2f")
    trump_win = format(trump_win, ".2f")
else:
    clinton_win = float(total / trials)
    trump_win = float(1 - clinton_win)

print("Chance of Trump winning: " + str(trump_win))
print("Chance of Clinton winning: " + str(clinton_win))

