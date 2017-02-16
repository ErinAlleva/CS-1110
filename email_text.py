# Alex Hicks (awh4kc)

import urllib.request

url = "http://www.sys.virginia.edu/people/faculty.html"

stream = urllib.request.urlopen(url)

for line in stream:
    text_to_search = line.decode("UTF-8").strip()

    if "mailto:" in text_to_search:
        start = (text_to_search.index("mailto:"))
        end = (text_to_search.rindex('"'))
        print(text_to_search[start + 7:end])

