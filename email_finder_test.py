# Alex Hicks (awh4kc)

import urllib.request
import re

def find_emails_in_website(url):
    stream = urllib.request.urlopen(url)
    intro_email_list = []
    regex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]{2,})")
    for line_number, line in enumerate(stream):
        decoded = transform(line, line_number)
        intro_email_list += regex.findall(decoded)
    email_list = []
    for email in intro_email_list:
        if email not in email_list:
            email_list.append(email)
    return email_list

def transform(line, index):
    replacements = [[" at ", "(at)", ". ", " dot ", " (dot)", "(dot)", "NOSPAM", "<br>"],
                    ["@", "@", " ", ".", ".", ".", "", ""]]
    decoded = line.decode("UTF-8")
    for i in range(len(replacements[0])):
        decoded = decoded.replace(replacements[0][i],replacements[1][i])
    decoded = decoded.strip().rstrip(".")
    if index == 31:
        decoded = decoded.replace("_",decoded[62])
    if index == 33:
        decoded = decoded[::-1]
    return decoded

print(find_emails_in_website("https://cs1110.cs.virginia.edu/emails.html"))

