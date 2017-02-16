# Alex Hicks (awh4kc)

import urllib.request

state = 'wisconsin'

stream = urllib.request.urlopen("http://elections.huffingtonpost.com/pollster/api/charts/2016-" + state +
                                    "-president-trump-vs-clinton.csv")

completed_after = '2016-09-11'
completed_before = '2016-10-27'

trump = []
clinton = []
dates = []
list_of_index = []
trump_score = []
clinton_score = []

for line in stream:
    decoded = line.decode("UTF-8")
    decoded = decoded.strip().split(",")
    if decoded[0] != "Trump":
        trump.append(decoded[0])
        clinton.append(decoded[1])
        dates.append(decoded[7])

list_of_dates = []
for j in range(len(dates)):
    if dates[j] >= completed_after and dates[j] <= completed_before:
        list_of_index.append(dates.index(dates[j]))
        list_of_dates.append(dates[j])

print(trump)

for i in list_of_index:
    trump_score.append(trump[i])
    clinton.remove(clinton[i])
    clinton_score.append(clinton[i])
    clinton.remove(clinton[i])

print(trump)

trump_score1 = [float(i) for i in trump_score]
clinton_score1 = [float(i) for i in clinton_score]

print(sum(trump_score1))
print(sum(clinton_score1))

sum_trump = format(sum(trump_score1) / int(len(trump_score1)),".2f")
sum_clinton = format(sum(clinton_score1) / int(len(clinton_score1)),".2f")

print(sum_trump)
print(sum_clinton)

