# Alex Hicks (awh4kc)

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

    trump_counter = 0
    clinton_counter = 0
    iterations = 0

    for list in list_thing:
        if list[7] >= completed_after and list[7] <= completed_before:
            trump_counter += float(list[0])
            clinton_counter += float(list[1])
            iterations += 1
    trump_avg = format(trump_counter/iterations, ".2f")
    clinton_avg = format(clinton_counter/iterations, ".2f")

    return [trump_avg, clinton_avg]