# Alex Hicks (awh4kc)

import urllib.request
import re

def find_emails_in_website(url):
    stream = urllib.request.urlopen(url)
    intro_email_list = []
    regex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]{2,})")
    for line in stream:
        decoded = transform(line)
        intro_email_list += regex.findall(decoded)
    email_list = []
    for email in intro_email_list:
        if email not in email_list:
            email_list.append(email)
    return email_list

def transform(line):
    replacements = [[" at ", "(at)", ". ", " dot ", " (dot)", "(dot)", "NOSPAM", "<br>"],
                    ["@", "@", " ", ".", ".", ".", "", ""]]
    decoded = line.decode("UTF-8")
    for i in range(len(replacements[0])):
        decoded = decoded.replace(replacements[0][i], replacements[1][i])
    decoded = decoded.strip().rstrip(".")
    return decoded

print(find_emails_in_website("https://cs1110.cs.virginia.edu/emails.html"))

