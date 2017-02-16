# Alex Hicks (awh4kc)

import urllib.request

#link = input("Gimme site: ")
link = "http://www.wunderground.com/history/airport/KCHO/2015/10/15/DailyHistory.html?format=1"

stream = urllib.request.urlopen(link)

for island in stream:
    decoded_island = island.decode("UTF-8")
    print(decoded_island.strip())

