# Alex Hicks (awh4kc)
# I received help from Kevin Naddoni (kn6vv)
# I received help from Michael Benos (mtb9ps)

def load_state_polls(state):

    import urllib.request

    if len(state.split()) > 1:
        state = state.replace(" ", "-")

    stream = urllib.request.urlopen( "http://elections.huffingtonpost.com/pollster/api/charts/2016-" + state +
                                     "-president-trump-vs-clinton.csv" )

    list_thing = []

    for line in stream:
        decoded = line.decode("UTF-8")
        decoded = decoded.strip().split(",")
        if decoded[0] != "Trump":
            list_thing.append(decoded)

    return list_thing

def polls_average(state,completed_after,completed_before):

    # import urllib.request
    #
    # if len(state.split()) > 1:
    #     state = state.replace(" ", "-")
    #
    # stream = urllib.request.urlopen("http://elections.huffingtonpost.com/pollster/api/charts/2016-" + state +
    #                                 "-president-trump-vs-clinton.csv")
    #
    # trump = []
    # clinton = []
    # dates = []
    # list_of_index = []
    # trump_score = []
    # clinton_score = []
    #
    # for line in stream:
    #     decoded = line.decode("UTF-8")
    #     decoded = decoded.strip().split(",")
    #     if decoded[0] != "Trump":
    #         trump.append(decoded[0])
    #         clinton.append(decoded[1])
    #         dates.append(decoded[7])
    #
    # for j in range(len(dates)):
    #     if dates[j] >= completed_after and dates[j] <= completed_before:
    #         list_of_index.append(dates.index(dates[j]))
    #
    # for i in list_of_index:
    #     trump_score.append(trump[i])
    #     trump.remove(trump[i])
    #     clinton_score.append(clinton[i])
    #     clinton.remove(clinton[i])
    #
    # trump_score1 = [float(i) for i in trump_score]
    # clinton_score1 = [float(i) for i in clinton_score]
    #
    # sum_trump = format(sum(trump_score1) / int(len(trump_score1)),".2f")
    # sum_clinton = format(sum(clinton_score1) / int(len(clinton_score1)),".2f")
    #
    # return [sum_trump, sum_clinton]

    import urllib.request

    if len(state.split()) > 1:
        state = state.replace(" ", "-")

    stream = urllib.request.urlopen("http://elections.huffingtonpost.com/pollster/api/charts/2016-" + state +
                                    "-president-trump-vs-clinton.csv")

    list_thing = []

    for line in stream:
        decoded = line.decode("UTF-8")
        decoded = decoded.strip().split(",")
        if decoded[0] != "Trump":
            list_thing.append(decoded)

    trumps = 0
    clintons = 0
    counts = 0

    for part_of_list_thing in list_thing:
        if part_of_list_thing[7] >= completed_after and part_of_list_thing[7] <= completed_before:
            trumps += float(part_of_list_thing[0])
            clintons += float(part_of_list_thing[1])
            counts += 1
    trump_avg = format(trumps / counts,".2f")
    clinton_avg = format(clintons / counts,".2f")

    return [trump_avg, clinton_avg]

def current_winner(poll):

    if poll[1] > poll[0]:
        answer = "Clinton +" + str(int(float(poll[1]) - float(poll[0])))
    elif poll[0] > poll[1]:
        answer = "Trump +" + str(int(float(poll[0]) - float(poll[1])))
    else:
        answer = "Tie"

    return answer

