# Alex Hicks (awh4kc)

import re
import urllib.request

def is_valid_password(password):
    regex = re.compile(r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$")
    results = regex.search(password)
    if results != None:
        return True
    return False

def find_possible_names(text):
    regex = re.compile(r"[A-Z][a-z]*")
    results = regex.search(text)
    if results != None:
        return results.group()
    return None

def find_all_possible_names(text):
    names = []

    regex = re.compile(r"[A-Z][a-z]*")
    results = regex.findall(text)
    if len(results) != 0:
        for name in results:
            names.append(name)
    return names

def find_all_phone_numbers(text):
    numbers = []

    regex = re.compile(r"[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]")
    results = regex.findall(text)
    if len(results) != 0:
        for number in results:
            numbers.append(number)

    return numbers

def find_phone_numbers_on_website(url):
    stream = urllib.request.urlopen(url)
    numbers = []

    for line in stream:
        decoded = line.decode("UTF-8").strip()
        numbers += find_all_phone_numbers(decoded)
    return numbers

print(is_valid_password("password"))
print(is_valid_password("abCd723223"))
print(find_possible_names("some text before Mark and more"))
print(find_possible_names("some text before Mark and Bob stuff"))
print(find_all_possible_names("some text before Mark and Bob stuff"))
print(find_all_phone_numbers("askljaslkdf 434-982-2688 alksdjfla"))
print(find_phone_numbers_on_website("http://www.archives.gov/about/organization/telephone-list.html"))

