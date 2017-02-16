# Alex Hicks (awh4kc)

import urllib.request

url = "http://cs1110.cs.virginia.edu/alice.txt"

stream = urllib.request.urlopen(url)

line_count = 0
word_count = 0

for line in stream:
    decoded = line.decode("UTF-8").strip()
    if decoded != "":
        line_count += 1
    if "Alice" in decoded:
        print(decoded.find("Alice"))
        word_count += 1

print(str(word_count) + "/" + str(line_count))

